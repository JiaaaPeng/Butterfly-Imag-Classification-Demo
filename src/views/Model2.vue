<template>
  <div class="model-page">
    <div class="page-header">
      <h1>MobileNet 模型</h1>
      <div class="header-divider"></div>
      <p class="subtitle">轻量级移动端深度学习网络</p>
    </div>

    <div class="content-container">
      <section class="model-overview">
        <div class="overview-banner">
          <el-image :src="structureImg" alt="MobileNet结构图" fit="cover" />
          <div class="banner-content">
            <div class="banner-tag">移动优化</div>
            <h2>模型简介</h2>
            <p>
              MobileNet
              是专为移动设备优化的轻量级卷积神经网络，通过深度可分离卷积等创新技术，
              显著降低计算复杂度，实现了高效的蝴蝶识别。
            </p>
          </div>
        </div>
        <div class="key-features">
          <div class="feature-item">
            <div class="feature-icon">
              <el-icon><Cellphone /></el-icon>
            </div>
            <div class="feature-content">
              <span>移动端优化</span>
              <p>专为移动设备设计的轻量级架构</p>
            </div>
          </div>
          <div class="feature-item">
            <div class="feature-icon">
              <el-icon><Timer /></el-icon>
            </div>
            <div class="feature-content">
              <span>实时推理</span>
              <p>毫秒级的识别响应速度</p>
            </div>
          </div>
          <div class="feature-item">
            <div class="feature-icon">
              <el-icon><Cpu /></el-icon>
            </div>
            <div class="feature-content">
              <span>资源节省</span>
              <p>显著降低内存和计算需求</p>
            </div>
          </div>
        </div>
      </section>

      <section class="core-features">
        <h2>核心特性</h2>
        <div class="section-subtitle">轻量级移动端优化方案</div>
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
        <div class="section-subtitle">轻量级模型性能对比</div>
        <model-performance-charts
          :accuracy-chart-option="accuracyChartOption"
          :performance-chart-option="performanceChartOption"
          :performance-data="performanceData"
          comparison-label="相对基准"
        />
      </section>

      <section class="applications">
        <h2>应用场景</h2>
        <div class="section-subtitle">广泛的移动端应用支持</div>
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
              <el-button text type="success">
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
import { Cellphone, Timer, Cpu, ArrowRight } from "@element-plus/icons-vue";
import ModelPerformanceCharts from "@/components/ModelPerformanceCharts.vue";
import ModelFeatureCard from "@/components/ModelFeatureCard.vue";

// 图片资源
const structureImg = new URL(
  "../assets/models/mobilenet/structure.png",
  import.meta.url
).href;
const featuresImg = new URL(
  "../assets/models/mobilenet/features.png",
  import.meta.url
).href;
const applicationImg = new URL(
  "../assets/models/mobilenet/application.png",
  import.meta.url
).href;

const performanceData = [
  {
    metric: "分类准确率",
    value: "92.8%",
    comparison: "-2.8%",
  },
  {
    metric: "模型大小",
    value: "2.8M",
    comparison: "-45%",
  },
  {
    metric: "推理速度",
    value: "25ms",
    comparison: "-40%",
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
        { value: 92.8, name: "准确识别" },
        { value: 7.2, name: "识别误差" },
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
    data: ["模型大小", "计算量", "内存占用"],
  },
  yAxis: {
    type: "value",
    name: "相对标准模型的比例",
  },
  series: [
    {
      name: "MobileNet",
      type: "bar",
      data: [0.55, 0.6, 0.58],
      itemStyle: {
        color: "#67c23a",
      },
      label: {
        show: true,
        position: "top",
        formatter: "{c}x",
      },
    },
  ],
};

// 应用场景数据
const applications = [
  {
    title: "手机端识别",
    description: "实时蝴蝶识别APP应用",
    image: applicationImg,
  },
  {
    title: "边缘计算",
    description: "物联网设备集成应用",
    image: applicationImg,
  },
  {
    title: "实时监测",
    description: "生态环境监测系统",
    image: applicationImg,
  },
];

// 核心特性数据
const coreFeatures = [
  {
    title: "深度可分离卷积",
    tag: "创新",
    tagType: "success",
    description: "将标准卷积分解为深度卷积和逐点卷积，大幅降低计算量",
    details: [
      "计算量降低90%以上",
      "参数量显著减少",
      "保持特征提取能力",
      "支持实时推理部署",
    ],
    image: featuresImg,
  },
  {
    title: "宽度乘子",
    tag: "优化",
    tagType: "warning",
    description: "通过调整网络宽度实现模型大小和精度的平衡",
    details: [
      "灵活调整网络规模",
      "适应不同设备性能",
      "优化资源利用率",
      "平衡精度与效率",
    ],
    image: featuresImg,
  },
  {
    title: "网络压缩",
    tag: "高效",
    tagType: "info",
    description: "采用模型压缩技术，优化模型尺寸",
    details: [
      "智能权重剪枝优化",
      "网络结构重参数化",
      "模型量化加速推理",
      "低比特存储压缩",
    ],
    image: featuresImg,
  },
];
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

/* 核心特性��分 */
.features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.feature-card {
  height: 100%;
  transition: transform 0.3s;
}

.feature-image {
  height: 200px;
  margin-top: 16px;
  border-radius: 8px;
  overflow: hidden;
}

/* 性能分析部分 */
.charts-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.chart-card {
  padding: 20px;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.pie-chart,
.bar-chart {
  height: 300px;
}

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
  padding: 16px 0;
}

/* MobileNet 特有的题色样式 */
.header-divider {
  background: linear-gradient(90deg, #67c23a, #95d475);
}

.feature-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(103, 194, 58, 0.15);
}

.feature-item:hover .feature-icon {
  background: #67c23a;
}

.feature-item .el-icon {
  color: #67c23a;
}

.feature-item:hover .el-icon {
  color: #fff;
}

/* 响应式设计 */
@media (max-width: 1024px) {
  .key-features,
  .features-grid,
  .applications-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .charts-container {
    grid-template-columns: 1fr;
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

/* 新增和修改的样式 */
.banner-tag {
  display: inline-block;
  padding: 4px 12px;
  background: rgba(103, 194, 58, 0.9);
  border-radius: 16px;
  font-size: 0.9em;
  margin-bottom: 16px;
}

.section-subtitle {
  text-align: center;
  color: #909399;
  margin: -20px 0 30px;
}

.feature-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.feature-card {
  padding: 20px;
}

.feature-card h3 {
  margin: 0;
  font-size: 1.2em;
  color: #303133;
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

.el-button.is-text:hover {
  color: #85ce61;
}

/* 优化响应式布局 */
@media (max-width: 1024px) {
  .performance-content {
    flex-direction: column;
  }

  .chart-card {
    margin-bottom: 20px;
  }
}

@media (max-width: 768px) {
  .banner-content {
    padding: 20px;
  }

  .banner-content h2 {
    font-size: 1.5em;
  }

  .section-subtitle {
    margin: -10px 0 20px;
    font-size: 0.9em;
  }
}
</style> 