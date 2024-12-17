<template>
  <el-card class="feature-card" :class="{ 'is-expanded': isExpanded }">
    <div class="feature-header">
      <h3>{{ title }}</h3>
      <el-tag size="small" :type="tagType">{{ tag }}</el-tag>
    </div>
    <div class="feature-content">
      <div class="feature-text">
        <p class="description">{{ description }}</p>
        <ul class="feature-details">
          <li v-for="detail in details" :key="detail">{{ detail }}</li>
        </ul>
      </div>
      <div class="feature-image" @click="isExpanded = !isExpanded">
        <el-image :src="image" fit="cover">
          <template #placeholder>
            <div class="image-placeholder">
              <el-icon><Picture /></el-icon>
            </div>
          </template>
        </el-image>
        <div class="image-overlay">
          <el-icon><ZoomIn /></el-icon>
        </div>
      </div>
    </div>
  </el-card>
</template>

<script setup>
import { ref, defineProps } from "vue";
import { Picture, ZoomIn } from "@element-plus/icons-vue";

defineProps({
  title: {
    type: String,
    required: true,
  },
  tag: {
    type: String,
    required: true,
  },
  tagType: {
    type: String,
    default: "info",
  },
  description: {
    type: String,
    required: true,
  },
  details: {
    type: Array,
    default: () => [],
  },
  image: {
    type: String,
    required: true,
  },
});

const isExpanded = ref(false);
</script>

<style scoped>
.feature-card {
  height: 100%;
  transition: all 0.3s ease;
  padding: 20px;
  position: relative;
  overflow: hidden;
  border: none;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.feature-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.feature-header h3 {
  margin: 0;
  font-size: 1.2em;
  color: #303133;
}

.feature-content {
  display: flex;
  flex-direction: column;
  gap: 16px;
  min-height: 200px;
}

.feature-text {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.description {
  color: #606266;
  line-height: 1.6;
  margin: 0;
  flex: none;
}

.feature-details {
  list-style: none;
  padding: 0;
  margin: 0;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.feature-details li {
  position: relative;
  padding-left: 20px;
  color: #606266;
  font-size: 0.9em;
  line-height: 1.5;
  transition: all 0.3s ease;
}

.feature-details li:hover {
  transform: translateX(4px);
  color: #409eff;
}

.feature-details li::before {
  content: "•";
  position: absolute;
  left: 0;
  color: #409eff;
  font-weight: bold;
}

.feature-image {
  position: relative;
  height: 160px;
  border-radius: 8px;
  overflow: hidden;
  cursor: pointer;
  margin-top: auto;
}

.feature-image :deep(.el-image) {
  width: 100%;
  height: 100%;
  transition: transform 0.3s ease;
}

.image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.image-overlay .el-icon {
  font-size: 24px;
  color: white;
}

.feature-image:hover .image-overlay {
  opacity: 1;
}

.feature-image:hover :deep(.el-image) {
  transform: scale(1.05);
}

.image-placeholder {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f5f7fa;
  color: #909399;
}

.is-expanded .feature-image {
  height: 240px;
}

@media (max-width: 768px) {
  .feature-image {
    height: 140px;
  }

  .is-expanded .feature-image {
    height: 200px;
  }
}
</style> 