<template>
  <div class="history-page">
    <div class="page-header">
      <h1>图像识别发展历程</h1>
      <p>探索从传统计算机视觉到深度学习的技术演进之路</p>
      <div class="header-divider"></div>
    </div>

    <div class="timeline-container">
      <el-timeline class="horizontal-timeline">
        <el-timeline-item
          v-for="(event, index) in timelineEvents"
          :key="index"
          :timestamp="event.time"
          placement="bottom"
          class="timeline-item"
        >
          <el-card class="timeline-card">
            <div class="card-content">
              <div class="card-main">
                <div class="card-header">
                  <h4>{{ event.title }}</h4>
                  <div class="card-tags">
                    <el-tag
                      v-for="tag in event.tags"
                      :key="tag"
                      size="small"
                      effect="plain"
                      class="tag-item"
                    >
                      {{ tag }}
                    </el-tag>
                  </div>
                </div>
                <div class="image-section">
                  <div class="image-wrapper">
                    <el-image
                      :src="event.image"
                      :alt="event.title"
                      class="timeline-image"
                      fit="cover"
                    >
                      <template #placeholder>
                        <div class="image-placeholder">
                          <el-icon><Picture /></el-icon>
                        </div>
                      </template>
                    </el-image>
                  </div>
                </div>
              </div>
              <div class="text-content">
                <p class="description">{{ event.description }}</p>
                <ul v-if="event.details">
                  <li v-for="detail in event.details" :key="detail">
                    {{ detail }}
                  </li>
                </ul>
              </div>
            </div>
          </el-card>
        </el-timeline-item>
      </el-timeline>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { Picture } from "@element-plus/icons-vue";

// 导入图片
import originImg from "../assets/history/origin.png";
import traditionalImg from "../assets/history/traditional.png";
import alexnetImg from "../assets/history/alexnet.png";
import resnetImg from "../assets/history/resnet.png";
import mobilenetImg from "../assets/history/mobilenet.png";
import efficientnetImg from "../assets/history/efficientnet.png";
import applicationImg from "../assets/history/application.png";

const timelineEvents = ref([
  {
    time: "1960s",
    title: "计算机视觉的起源",
    tags: ["开创时期", "基础研究"],
    description: "首次尝试使用计算机处理和分析图像，开启了计算机视觉的研究领域",
    details: [
      "Roberts算子的提出，开创了边缘检测的先河",
      "首次提出数字图像处理的概念",
      "开始探索模式识别的基本理论",
    ],
    image: originImg,
  },
  {
    time: "1980s-1990s",
    title: "传统图像处理时代",
    tags: ["特征工程", "传统算法"],
    description:
      "使用人工设的特征提取器和分类器进行图像识别，如SIFT、HOG等算法",
    details: [
      "SIFT特征的提出revolutionized特征提取方法",
      "HOG描述子在目标检测中的广泛应用",
      "基于规则的图像分割和识别算法的发展",
    ],
    image: traditionalImg,
  },
  {
    time: "2012",
    title: "深度学习革命 - AlexNet",
    tags: ["深度学习", "CNN"],
    description: "AlexNet在ImageNet竞赛中取得突破性成果，掀起深度学习革命",
    details: [
      "首次在大规模数据集上证明深度学习的有效性",
      "使用ReLU激活函数解决梯度消失问题",
      "引入Dropout防止过拟合",
    ],
    image: alexnetImg,
  },
  {
    time: "2015",
    title: "残差网络 - ResNet",
    tags: ["残差学习", "超深网络"],
    description:
      "ResNet提出残差连接结构，成功训练超深层网络，大幅提升识别准确率",
    details: [
      "通过残差连接解决深层网络的退化问题",
      "成功训练152层深度的网络结构",
      "在ILSVRC 2015竞赛中获得冠军",
    ],
    image: resnetImg,
  },
  {
    time: "2017",
    title: "移动端优化 - MobileNet",
    tags: ["轻量级", "动优化"],
    description: "专为移动设备优化的轻量级网络架构，平衡性能与效率",
    details: [
      "使用深度可分离卷积减少计算量",
      "引入宽度乘子控制模型大小",
      "在移动设备上实现实时推理",
    ],
    image: mobilenetImg,
  },
  {
    time: "2019",
    title: "高效网络 - EfficientNet",
    tags: ["复合缩放", "高效架构"],
    description: "提出复合缩放方法，在准确率和计算效率之间取得最佳平衡",
    details: [
      "提出网络深度、宽度、分辨率的复合缩放方法",
      "以更少的参数量实现更的准确率",
      "建立移动端到服务器端的统一架构",
    ],
    image: efficientnetImg,
  },
  {
    time: "现在",
    title: "多样化应用",
    tags: ["实际应用", "蝴蝶识别"],
    description: "图像识别技术广泛应用于各个领域，包括我们的蝴蝶识别系统",
    details: [
      "支持多种蝴蝶品种的精确识别",
      "结合多个先进模型提供准确预测",
      "持续化和更新识别能力",
    ],
    image: applicationImg,
  },
]);
</script>

<style scoped>
.history-page {
  padding: 80px 20px 40px;
  max-width: 1200px;
  margin: 0 auto;
  background-color: #ffffff;
}

.page-header {
  text-align: center;
  margin-bottom: 60px;
  position: relative;
}

.header-divider {
  width: 60px;
  height: 4px;
  background: #409eff;
  margin: 20px auto;
  border-radius: 2px;
}

.page-header h1 {
  font-size: 2.8em;
  color: #303133;
  margin-bottom: 16px;
  font-weight: 600;
}

.page-header p {
  font-size: 1.4em;
  color: #606266;
}

.timeline-container {
  position: relative;
  padding: 40px;
  background: linear-gradient(to bottom, #f5f7fa 0%, #ffffff 100%);
  border-radius: 12px;
  margin: 0 auto;
  overflow-x: auto;
}

.horizontal-timeline {
  display: flex;
  flex-direction: row;
  min-width: min-content;
  padding: 20px 0;
}

.timeline-item {
  flex: 0 0 auto;
  width: 400px;
  margin-right: 40px;
}

.card-content {
  display: grid;
  grid-template-rows: auto 1fr;
  gap: 16px;
}

.card-main {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0;
}

.card-tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.tag-item {
  border-radius: 16px;
  padding: 2px 12px;
}

.image-section {
  position: relative;
  padding: 8px;
  background: #f5f7fa;
  border-radius: 12px;
  width: 100%;
  margin: 0 auto;
}

.image-wrapper {
  width: 100%;
  aspect-ratio: 4/3;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.timeline-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s;
}

.image-wrapper:hover .timeline-image {
  transform: scale(1.05);
}

.text-content {
  padding: 0;
}

.description {
  font-size: 1.1em;
  line-height: 1.6;
  color: #303133;
  margin-bottom: 16px;
}

.text-content ul {
  margin-top: 12px;
  padding-left: 24px;
  color: #606266;
}

.text-content li {
  margin: 8px 0;
  line-height: 1.6;
  position: relative;
}

.text-content li::marker {
  color: #409eff;
}

:deep(.el-timeline-item__node) {
  background-color: #409eff;
  border: 4px solid #fff;
  box-shadow: 0 0 0 2px #409eff;
  transform: scale(1.2);
}

:deep(.el-timeline-item__tail) {
  top: 0;
  height: 4px;
  width: 100%;
  left: 0;
  transform: translateY(10px);
}

.el-card {
  transition: transform 0.3s;
  margin: 0 auto;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.el-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

@media (max-width: 768px) {
  .timeline-container {
    padding: 20px;
  }

  .timeline-item {
    width: 300px;
    margin-right: 20px;
  }

  .image-wrapper {
    aspect-ratio: 3/2;
  }
}
</style> 