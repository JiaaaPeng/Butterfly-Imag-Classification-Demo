import json
import base64
import io
from http.server import HTTPServer, BaseHTTPRequestHandler
from PIL import Image
import torch
import torchvision.transforms as transforms
from models import EfficientNet, MobileNet, ResNet
from utils.preprocess import preprocess_image

class ButterflyClassifier:
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.models = self._load_models()
        self.labels = self._load_labels()
        
    def _load_models(self):
        models = {
            'efficientnet': EfficientNet().to(self.device),
            'mobilenet': MobileNet().to(self.device),
            'resnet': ResNet().to(self.device)
        }
        # 加载模型权重
        for name, model in models.items():
            try:
                model.load_state_dict(torch.load(f'weights/{name}.pth'))
                model.eval()
            except Exception as e:
                print(f"Warning: Could not load {name} weights: {e}")
        return models
    
    def _load_labels(self):
        try:
            with open('utils/butterfly_labels.txt', 'r', encoding='utf-8') as f:
                return [line.strip() for line in f.readlines()]
        except:
            return [f"Butterfly_{i}" for i in range(10)]
    
    def predict(self, image):
        results = {}
        with torch.no_grad():
            for name, model in self.models.items():
                outputs = model(image.to(self.device))
                probs = torch.nn.functional.softmax(outputs, dim=1)[0]
                top3_prob, top3_idx = torch.topk(probs, 3)
                
                results[name] = [
                    (self.labels[idx], prob.item())
                    for idx, prob in zip(top3_idx, top3_prob)
                ]
        return results

class RequestHandler(BaseHTTPRequestHandler):
    classifier = ButterflyClassifier()
    
    def _send_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
    
    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()
    
    def do_POST(self):
        if self.path != '/predict':
            self.send_error(404)
            return
            
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            # 处理图像数据
            image_data = data['image']
            if 'base64,' in image_data:
                image_data = image_data.split('base64,')[1]
            image_bytes = base64.b64decode(image_data)
            image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
            
            # 预处理图像
            image_tensor = preprocess_image(image)
            
            # 获取预测结果
            predictions = self.classifier.predict(image_tensor)
            
            # 格式化响应
            response = []
            for model_name, preds in predictions.items():
                result = [model_name]
                for label, prob in preds:
                    result.extend([label, f"{prob:.3f}"])
                response.append(','.join(result))
            
            # 发送响应
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write('\n'.join(response).encode())
            
        except Exception as e:
            print(f"Error processing request: {e}")
            self.send_error(500, str(e))

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server() 