from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
import base64
from predict import predict_image

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.project_root = os.path.abspath(os.path.join(self.current_dir, '../..'))
        self.is_processing = False
        super().__init__(*args, **kwargs)

    def end_headers(self):
        """添加 CORS 头部"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Access-Control-Max-Age', '86400')
        super().end_headers()

    def do_OPTIONS(self):
        """处理预检请求"""
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        if self.path == '/predict':
            try:
                print(f"收到预测请求，当前处理状态: {self.is_processing}")
                if self.is_processing:
                    print("已有请求正在处理，拒绝新请求")
                    self.send_response(429)
                    self.end_headers()
                    self.wfile.write(json.dumps({
                        'error': '正在处理上一个请求，请稍后再试'
                    }).encode())
                    return

                self.is_processing = True
                print("开始处理预测请求...")
                
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))
                
                print("解码图片数据...")
                img_data = base64.b64decode(data['image'].split(',')[1])
                
                temp_path = os.path.join(self.current_dir, 'temp_image.jpg')
                print(f"保存临时文件到: {temp_path}")
                
                with open(temp_path, 'wb') as f:
                    f.write(img_data)
                
                print("开始执行预测...")
                success = predict_image(temp_path)
                
                print(f"预测结果: {'成功' if success else '失败'}")
                
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                
                if success:
                    result_path = os.path.join(self.project_root, 'public/outputs/predictions/predictions.csv')
                    print(f"读取预测结果: {result_path}")
                    
                    with open(result_path, 'r') as f:
                        predictions = f.read()
                    
                    response_data = predictions.encode()
                    
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain')
                    self.send_header('Content-Length', str(len(response_data)))
                    self.end_headers()
                    
                    print("发送预测结果...")
                    try:
                        self.wfile.write(response_data)
                        self.wfile.flush()
                        print("预测结果发送完成")
                    except (BrokenPipeError, ConnectionResetError) as e:
                        print(f"发送数据时连接断开: {str(e)}")
                        return
                else:
                    raise Exception("预测失败")
                    
            except Exception as e:
                print(f"错误详情: {str(e)}")
                print(f"错误类型: {type(e)}")
                import traceback
                print(f"错误堆栈: {traceback.format_exc()}")
                
                self.send_response(500)
                self.end_headers()
                error_message = {
                    'error': str(e),
                    'traceback': traceback.format_exc()
                }
                self.wfile.write(json.dumps(error_message).encode())
            finally:
                try:
                    self.wfile.flush()
                except:
                    pass
                print("重置处理状态...")
                self.is_processing = False
                print("请求处理完成")
        else:
            self.send_response(404)
            self.end_headers()

    def handle_error(self, request, client_address):
        """重写错误处理方法，避免在连接断开时打印堆栈跟踪"""
        print(f"处理请求时发生错误: {client_address}")

def run_server(port=8000):
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, CORSRequestHandler)
    print(f'Starting server on http://127.0.0.1:{port}')
    httpd.serve_forever()

if __name__ == '__main__':
    try:
        run_server()
    except Exception as e:
        print(f"服务器启动失败: {str(e)}")