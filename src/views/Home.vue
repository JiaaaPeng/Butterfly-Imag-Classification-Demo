<template>
  <div class="home">
    <!-- 头部横幅 -->
    <section class="hero">
      <div class="hero-content">
        <h1>蝴蝶智能识别系统</h1>
        <p>基于深度学习的智能蝴蝶识别与分类平台，支持多种蝴蝶品种的精确识别</p>
        <router-link to="/demo" class="try-button">
          <el-button type="primary" size="large">立即体验</el-button>
        </router-link>
      </div>
    </section>

    <!-- 特点介绍 -->
    <section class="features">
      <h2 class="section-title">核心特点</h2>
      <div class="features-grid">
        <div class="feature-card">
          <el-icon class="feature-icon"><Monitor /></el-icon>
          <h3>专业识别</h3>
          <p>支持100种蝴蝶品种的精确识别与分类</p>
        </div>
        <div class="feature-card">
          <el-icon class="feature-icon"><Lightning /></el-icon>
          <h3>实时识别</h3>
          <p>快速准确的识别引擎，秒级返回分析结果</p>
        </div>
        <div class="feature-card">
          <el-icon class="feature-icon"><DataAnalysis /></el-icon>
          <h3>详细信息</h3>
          <p>提供蝴蝶的详细特征、习性和分布信息</p>
        </div>
        <div class="feature-card">
          <el-icon class="feature-icon"><Connection /></el-icon>
          <h3>数据共享</h3>
          <p>支持识别结果导出与数据分享功能</p>
        </div>
      </div>
    </section>

    <!-- 模型展示 -->
    <section class="models">
      <h2 class="section-title">支持的模型</h2>
      <div class="model-cards">
        <el-card v-for="model in models" :key="model.id" class="model-card">
          <img :src="model.image" :alt="model.name" class="model-image" />
          <h3>{{ model.name }}</h3>
          <p>{{ model.description }}</p>
          <router-link :to="model.path">
            <el-button type="primary" plain>了解更多</el-button>
          </router-link>
        </el-card>
      </div>
    </section>

    <!-- 技术优势 -->
    <section class="advantages">
      <h2 class="section-title">技术优势</h2>
      <div class="advantages-content">
        <div class="advantage-text">
          <h3>专业的蝴蝶识别技术</h3>
          <ul>
            <li>准确率超过95%的识别模型</li>
            <li>支持多角度蝴蝶图像识别</li>
            <li>持续更新的品种数据库</li>
            <li>专业的分类学专家团队支持</li>
          </ul>
        </div>
        <div class="advantage-image">
          <img :src="techIllustrationImage" alt="技术优势" />
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from "vue";
import {
  Monitor,
  Lightning,
  DataAnalysis,
  Connection,
} from "@element-plus/icons-vue";

const models = ref([
  {
    id: 1,
    name: "EfficientNet",
    description:
      "高效准确的蝴蝶识别模型，平衡计算资源与识别精度，适合日常观察使用",
    image: new URL("../assets/efficientnet.png", import.meta.url).href,
    path: "/model1",
  },
  {
    id: 2,
    name: "MobileNet",
    description: "轻量级蝴蝶识别模型，优化移动端性能，提供快速识别服务",
    image: new URL("../assets/mobilenet.png", import.meta.url).href,
    path: "/model2",
  },
  {
    id: 3,
    name: "ResNet",
    description:
      "深度残差网络模型，强大的特征提取能力，提供高精度的蝴蝶分类结果",
    image: new URL("../assets/resnet.png", import.meta.url).href,
    path: "/model3",
  },
]);

const techIllustrationImage = new URL("../assets/tech.png", import.meta.url)
  .href;
</script>

<style scoped>
.home {
  padding-top: 20px;
}

.hero {
  height: 500px;
  background: linear-gradient(135deg, #1890ff 0%, #36cfc9 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  margin-bottom: 40px;
}

.hero-content {
  max-width: 800px;
  padding: 0 20px;
}

.hero h1 {
  font-size: 3em;
  margin-bottom: 20px;
}

.hero p {
  font-size: 1.2em;
  margin-bottom: 30px;
}

.section-title {
  text-align: center;
  font-size: 2em;
  margin-bottom: 40px;
  color: #303133;
}

.features {
  padding: 40px 20px;
  background-color: #f5f7fa;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
  max-width: 1200px;
  margin: 0 auto;
}

.feature-card {
  text-align: center;
  padding: 30px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.feature-icon {
  font-size: 40px;
  color: #409eff;
  margin-bottom: 20px;
}

.models {
  padding: 40px 20px;
}

.model-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  max-width: 1200px;
  margin: 0 auto;
}

.model-card {
  text-align: center;
}

.model-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  margin-bottom: 20px;
}

.advantages {
  padding: 40px 20px;
  background-color: #f5f7fa;
}

.advantages-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  max-width: 1200px;
  margin: 0 auto;
  align-items: center;
}

.advantage-text ul {
  list-style: none;
  padding: 0;
}

.advantage-text li {
  margin: 15px 0;
  padding-left: 30px;
  position: relative;
}

.advantage-text li::before {
  content: "✓";
  position: absolute;
  left: 0;
  color: #409eff;
}

.advantage-image img {
  width: 100%;
  border-radius: 8px;
}

@media (max-width: 768px) {
  .hero {
    height: 400px;
  }

  .hero h1 {
    font-size: 2em;
  }

  .advantages-content {
    grid-template-columns: 1fr;
  }
}
</style> 