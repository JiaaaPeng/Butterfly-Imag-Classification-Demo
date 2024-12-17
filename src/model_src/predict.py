# src/predict.py

import os
import torch
import torch.nn as nn
from torchvision import transforms
from torch.utils.data import DataLoader, Dataset
from PIL import Image
import pandas as pd
from tqdm import tqdm

from models.efficientnet_b0 import get_model as get_efficientnet_b0
from models.mobilenet_v3_large import get_model as get_mobilenet_v3_large
from models.resnet50 import get_model as get_resnet50


class ResizeAndPad:
    def __init__(self, size, fill=0):
        """
        Args:
            size (tuple or int): Desired output size. If tuple, output size will be matched to this. If int, smaller edge will be matched to this.
            fill (int or tuple): Pixel fill value for padding. Default: 0
        """
        if isinstance(size, int):
            self.size = (size, size)
        else:
            self.size = size
        self.fill = fill

    def __call__(self, img):
        # Get current and desired aspect ratios
        original_size = img.size  # (width, height)
        ratio = min(self.size[0] / original_size[0], self.size[1] / original_size[1])
        new_size = (int(original_size[0] * ratio), int(original_size[1] * ratio))
        img = img.resize(new_size, Image.BICUBIC)

        # Create a new image and paste the resized on it
        new_img = Image.new("RGB", self.size, (self.fill, self.fill, self.fill))
        paste_position = ((self.size[0] - new_size[0]) // 2,
                          (self.size[1] - new_size[1]) // 2)
        new_img.paste(img, paste_position)
        return new_img


def load_model(model, model_path, device='cpu'):
    """
    加载模型权重
    """
    model.load_state_dict(torch.load(model_path, map_location=device))
    model = model.to(device)
    model.eval()
    return model


def predict_image(image_path):
    """预测单张图片"""
    try:
        print(f"开始处理图片: {image_path}")
        
        # 获取当前文件的绝对路径
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, '../..'))
        
        # 设置输出目录
        output_dir = os.path.join(project_root, 'public/outputs/predictions')
        os.makedirs(output_dir, exist_ok=True)
        print(f"输出目录: {output_dir}")
        
        # 图像预处理
        test_transforms = transforms.Compose([
            ResizeAndPad((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406],
                               [0.229, 0.224, 0.225])
        ])
        
        print("加载图片...")
        # 加载图像
        image = Image.open(image_path).convert('RGB')
        image = test_transforms(image).unsqueeze(0)  # 添加 batch 维度

        # 加载类别名称
        class_names_path = os.path.join(project_root, 'class_names.txt')
        print(f"类别名称文件路径: {class_names_path}")
        
        with open(class_names_path, 'r') as f:
            class_names = [line.strip() for line in f.readlines()]
        
        # 设置设备
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"使用设备: {device}")
        image = image.to(device)

        # 模型路径
        models_dir = os.path.join(project_root, 'experiments')
        print(f"模型目录: {models_dir}")

        # 加载三个模型
        model1 = get_efficientnet_b0(len(class_names))
        model1_path = os.path.join(project_root, 'experiments/efficientnet_b0/checkpoints/best_model.pth')
        print(f"加载 EfficientNet 模型: {model1_path}")
        model1 = load_model(model1, model1_path, device)

        model2 = get_mobilenet_v3_large(len(class_names))
        model2_path = os.path.join(project_root, 'experiments/mobilenet_v3_large/checkpoints/best_model.pth')
        print(f"加载 MobileNet 模型: {model2_path}")
        model2 = load_model(model2, model2_path, device)

        model3 = get_resnet50(len(class_names))
        model3_path = os.path.join(project_root, 'experiments/resnet50/checkpoints/best_model.pth')
        print(f"加载 ResNet 模型: {model3_path}")
        model3 = load_model(model3, model3_path, device)

        # Softmax
        softmax = nn.Softmax(dim=1)

        # 预测
        results = []
        for model_name, model in [('efficientnet', model1), 
                              ('mobilenet', model2), 
                              ('resnet', model3)]:
            outputs = model(image)
            probs = softmax(outputs)
            top3_probs, top3_idxs = torch.topk(probs, k=3, dim=1)
            
            # 获取预测结果
            top3_prob = top3_probs[0].cpu().detach().numpy()
            top3_idx = top3_idxs[0].cpu().detach().numpy()
            top3_classes = [class_names[idx] for idx in top3_idx]
            
            # 计算其他类别的概率
            other_prob = 1.0 - top3_prob.sum()
            other_prob = max(other_prob, 0.0)
            
            # 保存结果
            results.append([
                model_name,
                top3_classes[0], round(float(top3_prob[0]), 2),
                top3_classes[1], round(float(top3_prob[1]), 2),
                top3_classes[2], round(float(top3_prob[2]), 2),
                round(float(other_prob), 2)
            ])
            
            # 为每个模型保存单独的预测结果
            model_results = pd.DataFrame([[
                top3_classes[0], round(float(top3_prob[0]), 2),
                top3_classes[1], round(float(top3_prob[1]), 2),
                top3_classes[2], round(float(top3_prob[2]), 2),
                round(float(other_prob), 2)
            ]])
            model_csv_path = os.path.join(output_dir, f'{model_name}_predictions.csv')
            model_results.to_csv(model_csv_path, index=False, header=False)

        # 保存总体结果
        df = pd.DataFrame(results)
        csv_path = os.path.join(output_dir, 'predictions.csv')
        df.to_csv(csv_path, index=False, header=False)
        return True

    except Exception as e:
        print(f"预测错误: {str(e)}")
        import traceback
        print(f"错误堆栈: {traceback.format_exc()}")
        return False


if __name__ == '__main__':
    main()