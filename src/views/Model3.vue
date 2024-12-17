<template>
  <div class="model-page">
    <div class="page-header">
      <h1>ResNet 模型</h1>
      <div class="header-divider"></div>
      <p class="subtitle">深度残差学习网络</p>
    </div>

    <div class="content-container">
      <section class="model-overview">
        <div class="overview-banner">
          <el-image :src="structureImg" alt="ResNet结构图" fit="cover" />
          <div class="banner-content">
            <div class="banner-tag">高精度</div>
            <h2>模型简介</h2>
            <p>
              ResNet 通过创新的残差学习结构解决了深层网络的退化问题，
              使得训练更深的网络成为可能。在蝴蝶识别任务中，
              其强大的特征提取能力确保了最高的识别准确率。
            </p>
          </div>
        </div>
        <div class="key-features">
          <div class="feature-item">
            <div class="feature-icon">
              <el-icon><Connection /></el-icon>
            </div>
            <div class="feature-content">
              <span>残差连接</span>
              <p>解决深层网络梯度消失问题</p>
            </div>
          </div>
          <div class="feature-item">
            <div class="feature-icon">
              <el-icon><Histogram /></el-icon>
            </div>
            <div class="feature-content">
              <span>深层特征</span>
              <p>强大的特征提取能力</p>
            </div>
          </div>
          <div class="feature-item">
            <div class="feature-icon">
              <el-icon><TrendCharts /></el-icon>
            </div>
            <div class="feature-content">
              <span>高精度</span>
              <p>业界领先的识别准确率</p>
            </div>
          </div>
        </div>
      </section>

      <section class="core-features">
        <h2>核心特性</h2>
        <div class="section-subtitle">深度学习的里程碑式创新</div>
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
        <div class="section-subtitle">卓越的识别性能</div>
        <model-performance-charts
          :accuracy-chart-option="accuracyChartOption"
          :performance-chart-option="performanceChartOption"
          :performance-data="performanceData"
          comparison-label="相对提升"
        />
      </section>

      <section class="applications">
        <h2>应用场景</h2>
        <div class="section-subtitle">广泛的高精度应用支持</div>
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
import {
  Connection,
  Histogram,
  TrendCharts,
  ArrowRight,
} from "@element-plus/icons-vue";
import ModelPerformanceCharts from "@/components/ModelPerformanceCharts.vue";
import ModelFeatureCard from "@/components/ModelFeatureCard.vue";

// 图片源
const structureImg = new URL(
  "../assets/models/resnet/structure.png",
  import.meta.url
).href;
const featuresImg = new URL(
  "../assets/models/resnet/features.png",
  import.meta.url
).href;
const applicationImg = new URL(
  "../assets/models/resnet/application.png",
  import.meta.url
).href;

const performanceData = [
  {
    metric: "分类准确率",
    value: "96.2%",
    comparison: "+3.1%",
  },
  {
    metric: "特征提取",
    value: "优秀",
    comparison: "基准",
  },
  {
    metric: "模型深度",
    value: "152层",
    comparison: "最深",
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
        { value: 96.2, name: "准确识别" },
        { value: 3.8, name: "识别误差" },
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
    data: ["特征提取", "分类准确率", "泛化能力"],
  },
  yAxis: {
    type: "value",
    name: "相对基准模型的比例",
  },
  series: [
    {
      name: "ResNet",
      type: "bar",
      data: [1.25, 1.31, 1.28],
      itemStyle: {
        color: "#8e44ad",
      },
      label: {
        show: true,
        position: "top",
        formatter: "{c}x",
      },
    },
  ],
};

// 核心特性数据
const coreFeatures = [
  {
    title: "残差学习",
    tag: "创新",
    tagType: "primary",
    description: "通过跳跃连接有效解决梯度消失问题，实现超深网络训练",
    details: [
      "优化梯度反向传播",
      "实现152层深度训练",
      "特征多尺度融合",
      "提升网络表达能力",
    ],
    image: featuresImg,
  },
  {
    title: "批量归一化",
    tag: "稳定",
    tagType: "warning",
    description: "加速网络收敛，提高训练稳定性",
    details: ["特征分布标准化", "加速模型收敛", "缓解梯度消失", "增强泛化能力"],
    image: featuresImg,
  },
  {
    title: "瓶颈结构",
    tag: "高效",
    tagType: "info",
    description: "优化计算效率，减少参数数量",
    details: [
      "三层卷积堆叠设计",
      "降维升维特征变换",
      "减少计算参数量",
      "提高信息密度",
    ],
    image: featuresImg,
  },
];

// 应用场景数据
const applications = [
  {
    title: "高精度识别",
    description: "适用于要求极高准确率的场景",
    image: applicationImg,
  },
  {
    title: "特征提取",
    description: "作为其他模型的骨干网络",
    image: applicationImg,
  },
  {
    title: "迁移学习",
    description: "优秀的迁移学习能力",
    image: applicationImg,
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

/* 核心特性部分 */
.features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin: 0 auto;
  max-width: 100%;
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
  padding: 20px;
}

/* 新增和修改的样式 */
.banner-tag {
  display: inline-block;
  padding: 4px 12px;
  background: rgba(142, 68, 173, 0.9);
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

/* ResNet 特有的主题色样式 */
.header-divider {
  background: linear-gradient(90deg, #8e44ad, #9b59b6);
}

.feature-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(142, 68, 173, 0.15);
}

.feature-item:hover .feature-icon {
  background: #8e44ad;
}

.feature-item .el-icon {
  color: #8e44ad;
}

.feature-item:hover .el-icon {
  color: #fff;
}

.el-button.is-text:hover {
  color: #9b59b6;
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
</style> 