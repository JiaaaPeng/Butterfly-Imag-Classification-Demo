<template>
  <div class="model-page">
    <div class="page-header">
      <h1>EfficientNet 模型</h1>
      <div class="header-divider"></div>
      <p class="subtitle">高效的复合缩放神经网络架构</p>
    </div>

    <div class="content-container">
      <section class="model-overview">
        <div class="overview-banner">
          <el-image :src="structureImg" alt="EfficientNet结构图" fit="cover" />
          <div class="banner-content">
            <div class="banner-tag">高效优化</div>
            <h2>模型简介</h2>
            <p>
              EfficientNet 是由 Google Research
              团队提出的一个卷积神经网络家族，通过复合缩放方法实现了更高的准确率和效率。
              在蝴蝶识别任务中，该模型表现出优秀的特征提取能力和计算效率。
            </p>
          </div>
        </div>
        <div class="key-features">
          <div class="feature-item">
            <div class="feature-icon">
              <el-icon><Cpu /></el-icon>
            </div>
            <div class="feature-content">
              <span>优化的计算效率</span>
              <p>通过复合缩放方法优化网络结构</p>
            </div>
          </div>
          <div class="feature-item">
            <div class="feature-icon">
              <el-icon><TrendCharts /></el-icon>
            </div>
            <div class="feature-content">
              <span>出色的准确率</span>
              <p>在蝴蝶识别任务中达到95%以上准确率</p>
            </div>
          </div>
          <div class="feature-item">
            <div class="feature-icon">
              <el-icon><Histogram /></el-icon>
            </div>
            <div class="feature-content">
              <span>平衡的资源利用</span>
              <p>在计算资源和性能间取得最佳平衡</p>
            </div>
          </div>
        </div>
      </section>

      <section class="core-features">
        <h2>核心特性</h2>
        <div class="section-subtitle">创新的网络优化方案</div>
        <div class="features-grid">
          <model-feature-card
            v-for="feature in coreFeatures"
            :key="feature.title"
            v-bind="feature"
          />
        </div>
      </section>

      <section class="performance">
        <h2>性能分析</h2>
        <div class="section-subtitle">优异的综合表现</div>
        <model-performance-charts
          :accuracy-chart-option="accuracyChartOption"
          :performance-chart-option="performanceChartOption"
          :performance-data="performanceData"
          comparison-label="相对提升"
        />
      </section>

      <section class="applications">
        <h2>应用场景</h2>
        <div class="section-subtitle">广泛的实际应用支持</div>
        <div class="applications-grid">
          <el-card
            v-for="app in applications"
            :key="app.title"
            class="app-card"
            :body-style="{ padding: '0px' }"
          >
            <div class="app-image">
              <el-image :src="app.image" fit="cover" />
            </div>
            <div class="app-content">
              <h3>{{ app.title }}</h3>
              <p>{{ app.description }}</p>
              <el-button text type="primary">
                了解更多
                <el-icon class="el-icon--right"><ArrowRight /></el-icon>
              </el-button>
            </div>
          </el-card>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import ModelPerformanceCharts from "@/components/ModelPerformanceCharts.vue";
import ModelFeatureCard from "@/components/ModelFeatureCard.vue";
import {
  Cpu,
  TrendCharts,
  Histogram,
  ArrowRight,
} from "@element-plus/icons-vue";

// 图片资源
const structureImg = new URL(
  "../assets/models/efficientnet/structure.png",
  import.meta.url
).href;
const featuresImg = new URL(
  "../assets/models/efficientnet/features.png",
  import.meta.url
).href;
const applicationImg = new URL(
  "../assets/models/efficientnet/application.png",
  import.meta.url
).href;

// 核心特性数据
const coreFeatures = [
  {
    title: "复合缩放方法",
    tag: "创新",
    tagType: "primary",
    description: "统一缩放网络深度、宽度和分辨率，实现最优性能平衡",
    details: [
      "自动搜索最佳网络配置",
      "平衡计算资源与模型性能",
      "支持多种硬件平台部署",
      "灵活的缩放系数调整",
    ],
    image: featuresImg,
  },
  {
    title: "MBConv模块",
    tag: "优化",
    tagType: "warning",
    description: "使用改进的MBConv模块提升特征提取能力",
    details: [
      "深度可分离卷积设计",
      "优化的瓶颈结构",
      "SE注意力机制增强",
      "残差连接保证稳定性",
    ],
    image: featuresImg,
  },
  {
    title: "自适应优化",
    tag: "高效",
    tagType: "info",
    description: "根据计算资源自动调整网络结构",
    details: ["动态资源分配", "自适应计算优化", "智能网络裁剪", "性能实时监控"],
    image: featuresImg,
  },
];

const performanceData = [
  {
    metric: "分类准确率",
    value: "95.6%",
    comparison: "+2.3%",
  },
  {
    metric: "参数量",
    value: "5.3M",
    comparison: "-23%",
  },
  {
    metric: "推理时间",
    value: "45ms",
    comparison: "-15%",
  },
];

// 应用场景数据
const applications = [
  {
    title: "移动端部署",
    description: "优化的模型结构使其非常适合在移动设备上运行",
    image: applicationImg,
  },
  {
    title: "在线服务",
    description: "云端API服务，快速响应",
    image: applicationImg,
  },
  {
    title: "批量处理",
    description: "高效的资源利用使其适合大规模数据处理",
    image: applicationImg,
  },
];

// 饼图配置
const accuracyChartOption = {
  tooltip: {
    trigger: "item",
  },
  legend: {
    orient: "vertical",
    right: 10,
    top: "center",
  },
  series: [
    {
      type: "pie",
      radius: ["40%", "70%"],
      avoidLabelOverlap: false,
      itemStyle: {
        borderRadius: 10,
        borderColor: "#fff",
        borderWidth: 2,
      },
      label: {
        show: false,
      },
      emphasis: {
        label: {
          show: true,
          fontSize: "14",
          fontWeight: "bold",
        },
      },
      data: [
        { value: 95.6, name: "准确识别" },
        { value: 4.4, name: "识别误差" },
      ],
    },
  ],
};

// 性能对比图配置
const performanceChartOption = {
  tooltip: {
    trigger: "axis",
    axisPointer: {
      type: "shadow",
    },
  },
  grid: {
    left: "3%",
    right: "4%",
    bottom: "3%",
    containLabel: true,
  },
  xAxis: {
    type: "category",
    data: ["参数量", "计算量", "推理时间"],
  },
  yAxis: {
    type: "value",
    name: "相对基准模型的比例",
  },
  series: [
    {
      name: "EfficientNet",
      type: "bar",
      data: [0.77, 0.68, 0.85],
      itemStyle: {
        color: "#409eff",
      },
      label: {
        show: true,
        position: "top",
        formatter: "{c}x",
      },
    },
  ],
};
</script>

<style scoped>
/* 继承基础样式 */
.model-page {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
  background: #ffffff;
}

.page-header {
  text-align: center;
  margin-bottom: 40px;
  position: relative;
}

.header-divider {
  width: 60px;
  height: 4px;
  margin: 20px auto;
  border-radius: 2px;
}

.subtitle {
  color: #606266;
  font-size: 1.2em;
  margin-top: 10px;
}

.content-container {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

section {
  padding: 30px;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease;
}

section:hover {
  transform: translateY(-5px);
}

/* 模型概述部分 */
.model-overview {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.overview-banner {
  position: relative;
  height: 360px;
  border-radius: 16px;
  overflow: hidden;
}

.banner-content {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 30px;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.7));
  color: white;
}

.banner-tag {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 16px;
  font-size: 0.9em;
  margin-bottom: 16px;
}

/* 特性卡片部分 */
.key-features {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.feature-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 24px;
  border-radius: 12px;
  background: #f5f7fa;
  transition: all 0.3s ease;
  height: 100%;
  min-height: 180px;
}

.feature-icon {
  width: 64px;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: #fff;
  margin-bottom: 16px;
  transition: all 0.3s ease;
}

.feature-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

/* .feature-content span {
  font-size: 1.1em;
  font-weight: 500;
  color: #303133;
}

.feature-content p {
  color: #606266;
  font-size: 0.9em;
  line-height: 1.6;
  margin: 0;
} */

/* 应用场景部分 */
.applications-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.app-card {
  transition: transform 0.3s;
}

.app-image {
  height: 200px;
  border-radius: 8px;
  overflow: hidden;
}

.app-content {
  padding: 20px;
}

.app-content h3 {
  margin: 0 0 8px;
  font-size: 1.1em;
  color: #303133;
}

.app-content p {
  margin: 0 0 16px;
  color: #606266;
  font-size: 0.9em;
  line-height: 1.6;
}

.el-button.is-text {
  padding: 0;
  height: auto;
  font-size: 0.9em;
}

/* EfficientNet 特有的主题色样式 */
.header-divider {
  background: linear-gradient(90deg, #409eff, #36cfc9);
}

.banner-tag {
  background: rgba(64, 158, 255, 0.9);
}

.feature-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(64, 158, 255, 0.15);
}

.feature-item:hover .feature-icon {
  background: #409eff;
}

.feature-item .el-icon {
  color: #409eff;
}

.feature-item:hover .el-icon {
  color: #fff;
}

.el-button.is-text:hover {
  color: #66b1ff;
}

.section-subtitle {
  text-align: center;
  color: #909399;
  margin: -20px 0 30px;
}

/* 响应式设计 */
@media (max-width: 1024px) {
  .key-features,
  .features-grid,
  .applications-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .key-features,
  .features-grid,
  .applications-grid {
    grid-template-columns: 1fr;
  }

  section {
    padding: 20px;
  }

  .overview-banner {
    height: 300px;
  }
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin: 0 auto;
  max-width: 100%;
}
</style> 