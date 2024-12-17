<template>
  <div class="performance-content">
    <div class="charts-container">
      <div class="chart-card">
        <h3>准确率分布</h3>
        <div class="pie-chart">
          <v-chart :option="accuracyChartOption" autoresize />
        </div>
      </div>
      <div class="chart-card">
        <h3>性能对比</h3>
        <div class="bar-chart">
          <v-chart :option="performanceChartOption" autoresize />
        </div>
      </div>
    </div>
    <div class="performance-metrics">
      <el-table :data="performanceData" stripe>
        <el-table-column prop="metric" label="指标" />
        <el-table-column prop="value" label="数值" />
        <el-table-column prop="comparison" :label="comparisonLabel" />
      </el-table>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from "vue";
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart, BarChart } from "echarts/charts";
import {
  GridComponent,
  TooltipComponent,
  LegendComponent,
} from "echarts/components";
import VChart from "vue-echarts";

use([
  CanvasRenderer,
  PieChart,
  BarChart,
  GridComponent,
  TooltipComponent,
  LegendComponent,
]);

defineProps({
  accuracyChartOption: {
    type: Object,
    required: true,
  },
  performanceChartOption: {
    type: Object,
    required: true,
  },
  performanceData: {
    type: Array,
    required: true,
  },
  comparisonLabel: {
    type: String,
    default: "相对提升",
  },
});
</script>

<style scoped>
.performance-content {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 24px;
}

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

.chart-card h3 {
  margin: 0 0 16px;
  font-size: 1.1em;
  color: #303133;
}

.pie-chart,
.bar-chart {
  height: 300px;
}

@media (max-width: 1024px) {
  .performance-content {
    grid-template-columns: 1fr;
  }

  .charts-container {
    grid-template-columns: 1fr;
  }

  .chart-card {
    margin-bottom: 20px;
  }
}
</style> 