<template>
  <div class="nav-container">
    <el-menu
      :default-active="activeIndex"
      class="nav-menu"
      mode="horizontal"
      router
      @select="handleSelect"
    >
      <div class="logo-container">
        <router-link to="/">
          <span class="logo-text">
            <el-icon class="logo-icon"><Picture /></el-icon>
            蝴蝶识别系统
          </span>
        </router-link>
      </div>

      <div class="menu-items">
        <el-menu-item index="/">
          <el-icon><HomeFilled /></el-icon>
          <span>首页</span>
        </el-menu-item>

        <el-sub-menu index="models">
          <template #title>
            <el-icon><Monitor /></el-icon>
            <span>模型介绍</span>
          </template>
          <el-menu-item index="/model1">EfficientNet</el-menu-item>
          <el-menu-item index="/model2">MobileNet</el-menu-item>
          <el-menu-item index="/model3">ResNet</el-menu-item>
        </el-sub-menu>

        <el-menu-item index="/history">
          <el-icon><Timer /></el-icon>
          <span>发展历程</span>
        </el-menu-item>
        <el-menu-item index="/demo">
          <el-icon><VideoPlay /></el-icon>
          <span>在线演示</span>
        </el-menu-item>
      </div>
    </el-menu>
  </div>
</template>

<script setup>
import { computed } from "vue";
import { useRoute } from "vue-router";
import {
  HomeFilled,
  Monitor,
  Timer,
  VideoPlay,
  Picture,
} from "@element-plus/icons-vue";

const route = useRoute();
const activeIndex = computed(() => route.path);

const handleSelect = (key) => {
  console.log(key);
};
</script>

<style scoped>
.nav-container {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background-color: white;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  height: 60px;
}

.nav-menu {
  display: flex;
  justify-content: space-between;
  height: 60px;
  padding: 0 20px;
  max-width: 1200px;
  margin: 0 auto;
  border-bottom: none;
}

.logo-container {
  display: flex;
  align-items: center;
  padding-right: 20px;
  min-width: 180px;
}

.logo-container a {
  display: flex;
  align-items: center;
  text-decoration: none;
  color: inherit;
}

.logo-text {
  font-size: 1.5em;
  font-weight: bold;
  color: #409eff;
  display: flex;
  align-items: center;
  gap: 8px;
  white-space: nowrap;
}

.logo-icon {
  font-size: 1.2em;
}

.menu-items {
  display: flex;
  flex: 1;
  justify-content: flex-end;
  gap: 10px;
}

:deep(.el-menu) {
  border-bottom: none !important;
}

:deep(.el-menu--horizontal) {
  border: none;
}

.el-menu-item [class^="el-icon"] {
  margin-right: 4px;
  font-size: 1.1em;
}

:deep(.el-sub-menu__title) {
  display: flex;
  align-items: center;
}

:deep(.el-sub-menu__icon-arrow) {
  margin-left: 4px;
}

.el-menu--horizontal > .el-menu-item,
.el-menu--horizontal > .el-sub-menu .el-sub-menu__title {
  height: 60px;
  line-height: 60px;
  padding: 0 16px;
  border-bottom: none;
}

.el-menu--horizontal > .el-menu-item.is-active {
  border-bottom: 2px solid #409eff;
  font-weight: 500;
  color: #409eff;
}

@media (max-width: 768px) {
  .nav-menu {
    padding: 0 10px;
  }

  .logo-text {
    font-size: 1.2em;
  }

  .el-menu--horizontal > .el-menu-item,
  .el-menu--horizontal > .el-sub-menu .el-sub-menu__title {
    padding: 0 12px;
  }

  .logo-container {
    min-width: 150px;
  }

  .menu-items {
    gap: 5px;
  }
}
</style> 