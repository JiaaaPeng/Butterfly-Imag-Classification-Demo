<template>
  <div class="demo-page">
    <div class="page-header">
      <h1>在线演示</h1>
      <p class="subtitle">上传图片，体验多模型识别效果</p>
    </div>

    <el-row :gutter="20">
      <el-col :span="8">
        <el-card class="upload-section">
          <template #header>
            <div class="card-header">
              <h3>图片上传</h3>
            </div>
          </template>

          <el-upload
            class="image-uploader"
            :show-file-list="false"
            :before-upload="beforeUpload"
            :auto-upload="false"
            accept="image/*"
            @change="handleFileChange"
          >
            <img v-if="imageUrl" :src="imageUrl" class="uploaded-image" />
            <div v-else class="upload-placeholder">
              <el-icon><Plus /></el-icon>
              <span>点击上传图片</span>
            </div>
          </el-upload>

          <div class="model-selection">
            <h4>选择模型</h4>
            <el-checkbox-group v-model="selectedModels">
              <el-checkbox value="efficientnet">EfficientNet</el-checkbox>
              <el-checkbox value="mobilenet">MobileNet</el-checkbox>
              <el-checkbox value="resnet">ResNet</el-checkbox>
            </el-checkbox-group>
          </div>

          <el-button
            type="primary"
            :disabled="!imageUrl || selectedModels.length === 0"
            :loading="analyzing"
            @click="startAnalysis"
          >
            开始分析
          </el-button>
        </el-card>

        <el-card v-if="lastImageUrl" class="last-upload-section">
          <template #header>
            <div class="card-header">
              <h3>预测对象</h3>
            </div>
          </template>
          <div class="last-image-container">
            <img :src="lastImageUrl" class="last-image" />
          </div>
        </el-card>
      </el-col>

      <el-col :span="16">
        <el-card v-if="hasResults" class="results-section">
          <template #header>
            <div class="card-header">
              <h3>识别结果</h3>
              <el-radio-group v-model="displayMode" size="small">
                <el-radio-button label="chart">图表</el-radio-button>
                <el-radio-button label="pie">饼图</el-radio-button>
                <el-radio-button label="table">表格</el-radio-button>
              </el-radio-group>
            </div>
          </template>

          <div v-if="displayMode === 'pie'" class="pie-container">
            <div
              v-for="model in selectedModels"
              :key="model"
              class="model-result"
            >
              <!-- <h4>{{ getModelName(model) + "模型" }}</h4> -->
              <v-chart class="pie-chart" :option="getPieOption(model)" />
            </div>
          </div>

          <div v-else-if="displayMode === 'chart'" class="chart-container">
            <div
              v-for="model in selectedModels"
              :key="model"
              class="model-result"
            >
              <h4>{{ getModelName(model) }}</h4>
              <div class="chart">
                <el-progress
                  v-for="(prob, index) in getTopPredictions(model)"
                  :key="index"
                  :percentage="Math.round(prob.probability * 100)"
                  :color="getModelColor(model)"
                >
                  <template #default="{ percentage }">
                    <span class="prediction-label">
                      {{ prob.label }}: {{ percentage }}%
                    </span>
                  </template>
                </el-progress>
              </div>
            </div>
          </div>

          <el-table
            v-else
            :data="tableData"
            style="width: 100%"
            :default-sort="{ prop: 'probability', order: 'descending' }"
          >
            <el-table-column prop="model" label="模型" width="120">
              <template #default="{ row }">
                <el-tag :type="getTagType(row.model)">{{
                  getModelName(row.model)
                }}</el-tag>
              </template>
            </el-table-column>
            <el-table-column prop="label" label="类别" />
            <el-table-column prop="probability" label="概率" width="100">
              <template #default="{ row }">
                {{ (row.probability * 100).toFixed(2) }}%
              </template>
            </el-table-column>
          </el-table>
        </el-card>

        <div v-else-if="imageUrl" class="placeholder-result">
          <el-icon><Loading /></el-icon>
          <p>请点击"开始分析"查看结果</p>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { Plus, Loading } from "@element-plus/icons-vue";
import { ElMessage } from "element-plus";
import { loadClassNames } from "../utils/modelUtils";
import { ref, computed, onMounted } from "vue";
import { onBeforeRouteLeave } from "vue-router";
import { provide } from "vue";
import VChart from "vue-echarts";
import { use } from "echarts/core";
import { PieChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
} from "echarts/components";
import { CanvasRenderer } from "echarts/renderers";

use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
]);

const imageUrl = ref("");
const lastImageUrl = ref("");
const analyzing = ref(false);
const selectedModels = ref(["efficientnet", "mobilenet", "resnet"]);
const displayMode = ref("chart");
const predictions = ref({});
const classNames = ref([]);
const uploadedImage = ref({
  file: null,
  base64: null,
  url: null,
});
const requestInProgress = ref(false);

provide("demoState", {
  analyzing,
  predictions,
  uploadedImage,
});

onMounted(() => {
  loadClassNames().then((names) => {
    classNames.value = names;
  });
  const lastImage = localStorage.getItem("lastImageUrl");
  if (lastImage) {
    lastImageUrl.value = lastImage;
  }
  const lastPredictions = localStorage.getItem("lastPredictions");
  if (lastPredictions) {
    try {
      predictions.value = JSON.parse(lastPredictions);
    } catch (e) {
      console.error("恢复预测结��失败:", e);
    }
  }
});

const beforeUpload = (file) => {
  const isImage = file.type.startsWith("image/");
  if (!isImage) {
    ElMessage.error("只能上传图片文件！");
    return false;
  }
  uploadedImage.value.file = file;

  const reader = new FileReader();
  reader.onload = () => {
    uploadedImage.value.base64 = reader.result;
    uploadedImage.value.url = URL.createObjectURL(file);
    imageUrl.value = uploadedImage.value.url;
  };
  reader.readAsDataURL(file);
  return false;
};

const startAnalysis = async () => {
  if (analyzing.value) return;
  if (requestInProgress.value) {
    ElMessage.warning("正在处理上一个请求，请稍后再试");
    return;
  }

  analyzing.value = true;
  requestInProgress.value = true;
  predictions.value = {};
  lastImageUrl.value = imageUrl.value;
  localStorage.setItem("lastImageUrl", imageUrl.value);

  try {
    if (!uploadedImage.value.base64) {
      throw new Error("请先上传图片");
    }

    console.log("发送预测请求...");

    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 30000); // 30秒超时

    const response = await fetch("http://localhost:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "text/plain",
      },
      body: JSON.stringify({
        image: uploadedImage.value.base64,
      }),
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`服务器错误: ${errorText}`);
    }

    const csvData = await response.text();
    console.log("接收预测结果...");

    const results = {};
    csvData
      .split("\n")
      .filter((line) => line.trim())
      .forEach((line) => {
        const [model, class1, prob1, class2, prob2, class3, prob3] =
          line.split(",");
        if (selectedModels.value.includes(model.toLowerCase())) {
          results[model.toLowerCase()] = [
            { label: class1, probability: parseFloat(prob1) },
            { label: class2, probability: parseFloat(prob2) },
            { label: class3, probability: parseFloat(prob3) },
          ];
        }
      });

    predictions.value = results;
    localStorage.setItem("lastPredictions", JSON.stringify(results));
    ElMessage.success("分析完成");
  } catch (error) {
    if (error.name === "AbortError") {
      console.error("请求超时");
      ElMessage.error("请求超时，请重试");
    } else {
      console.error("分析错误:", error);
      ElMessage.error(`分析失败: ${error.message}`);
    }
  } finally {
    analyzing.value = false;
    requestInProgress.value = false;
    console.log("分析请求完成");
  }
};

const hasResults = computed(() => {
  return Object.keys(predictions.value).length > 0;
});

const tableData = computed(() => {
  const data = [];
  Object.entries(predictions.value).forEach(([model, preds]) => {
    preds.forEach((pred) => {
      data.push({
        model,
        ...pred,
      });
    });
  });
  return data;
});

const getModelName = (model) => {
  const names = {
    efficientnet: "EfficientNet",
    mobilenet: "MobileNet",
    resnet: "ResNet",
  };
  return names[model];
};

const getModelColor = (model) => {
  const colors = {
    efficientnet: "#409EFF",
    mobilenet: "#67C23A",
    resnet: "#E6A23C",
  };
  return colors[model];
};

const getTagType = (model) => {
  const types = {
    efficientnet: "primary",
    mobilenet: "success",
    resnet: "warning",
  };
  return types[model];
};

const getTopPredictions = (model) => {
  return predictions.value[model]?.slice(0, 5) || [];
};

const handleFileChange = (uploadFile) => {
  predictions.value = {};
  uploadedImage.value.file = uploadFile.raw;
  const reader = new FileReader();
  reader.onload = (e) => {
    uploadedImage.value.base64 = e.target.result;
    uploadedImage.value.url = URL.createObjectURL(uploadFile.raw);
    imageUrl.value = uploadedImage.value.url;
  };
  reader.readAsDataURL(uploadFile.raw);
};

const getPieOption = (model) => {
  const modelData = predictions.value[model] || [];
  const data = modelData.map((item) => ({
    name: item.label,
    value: Math.round(item.probability * 100),
  }));

  // 计算其他类概率
  const sum = data.reduce((acc, item) => acc + item.value, 0);
  if (sum < 100) {
    data.push({
      name: "其他",
      value: 100 - sum,
    });
  }

  return {
    title: {
      text: getModelName(model),
      left: "center",
    },
    tooltip: {
      trigger: "item",
      formatter: "{b}: {c}%",
    },
    legend: {
      orient: "vertical",
      left: "left",
      top: "middle",
    },
    series: [
      {
        name: "预测结果",
        type: "pie",
        radius: ["40%", "70%"],
        avoidLabelOverlap: true,
        itemStyle: {
          borderRadius: 10,
          borderColor: "#fff",
          borderWidth: 2,
        },
        label: {
          show: false,
          position: "center",
        },
        emphasis: {
          label: {
            show: true,
            fontSize: "20",
            fontWeight: "bold",
          },
        },
        labelLine: {
          show: false,
        },
        data: data,
        color: [getModelColor(model), "#91cc75", "#fac858", "#ee6666"],
      },
    ],
  };
};

onBeforeRouteLeave((to, from, next) => {
  if (analyzing.value) {
    ElMessage.warning("请等待分析完成");
    next(false);
    return;
  }
  next();
});
</script>

<style scoped>
.demo-page {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.page-header {
  text-align: center;
  margin-bottom: 40px;
}

.page-header h1 {
  font-size: 2.5em;
  color: #303133;
  margin-bottom: 20px;
}

.subtitle {
  font-size: 1.2em;
  color: #606266;
}

.upload-section {
  margin-bottom: 20px;
}

.image-uploader {
  text-align: center;
}

.upload-placeholder {
  width: 100%;
  height: 150px;
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.upload-placeholder:hover {
  border-color: #409eff;
}

.upload-placeholder .el-icon {
  font-size: 28px;
  color: #8c939d;
  margin-bottom: 10px;
}

.uploaded-image {
  width: 100%;
  height: 150px;
  object-fit: contain;
}

.model-selection {
  margin: 15px 0;
}

.model-selection h4 {
  margin-bottom: 10px;
  color: #303133;
}

.results-section {
  height: 100%;
  min-height: 500px;
}

.chart-container {
  margin-top: 20px;
  padding: 0 40px;
}

.model-result {
  margin-bottom: 30px;
}

.model-result h4 {
  margin-bottom: 15px;
  color: #303133;
  font-size: 18px;
  text-align: center;
}

.chart {
  padding: 10px 30px;
}

.el-progress {
  margin-bottom: 20px;
}

:deep(.el-progress-bar__outer) {
  height: 24px !important;
}

:deep(.el-progress-bar__inner) {
  height: 24px !important;
}

.prediction-label {
  margin-left: 10px;
  color: #606266;
  font-size: 16px;
}

.placeholder-result {
  height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #909399;
}

.placeholder-result .el-icon {
  font-size: 48px;
  margin-bottom: 10px;
}

.last-upload-section {
  margin-bottom: 20px;
}

.last-image-container {
  text-align: center;
}

.last-image {
  width: 100%;
  height: 150px;
  object-fit: contain;
}

.pie-container {
  margin-top: 20px;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: space-around;
  padding: 20px;
}

.pie-container .model-result {
  flex: 0 0 calc(33.33% - 20px);
  min-width: 280px;
  margin-bottom: 0;
}

.pie-chart {
  height: 280px;
  width: 100%;
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 15px 20px;
  border-bottom: 1px solid #ebeef5;
}

.card-header h3 {
  margin: 0;
  font-size: 18px;
  color: #303133;
}

:deep(.el-table) {
  margin-top: 20px;
  font-size: 16px;
}

:deep(.el-table th) {
  font-size: 16px;
  background-color: #f5f7fa;
  padding: 12px 0;
}

:deep(.el-table td) {
  padding: 12px 0;
}

:deep(.el-tag) {
  font-size: 14px;
  padding: 6px 12px;
}
</style> 