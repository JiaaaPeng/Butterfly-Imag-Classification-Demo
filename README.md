# 蝴蝶智能识别系统

一个基于深度学习的蝴蝶图像识别系统，支持多种先进模型，提供直观的可视化界面和实时识别功能。

## 项目简介

本项目是一个完整的蝴蝶识别解决方案，集成了 EfficientNet、MobileNet 和 ResNet 三种深度学习模型，可以准确识别 100 种蝴蝶品种。系统提供了友好的 Web 界面，支持实时图像上传和多模型并行预测。

## 技术栈

### 前端
- Vue 3 (组合式 API)
- Element Plus UI 框架
- ECharts 图表库
- Vue Router 路由管理
- Vite 构建工具

### 后端
- Python HTTP Server
- 深度学习框架支持
  - EfficientNet
  - MobileNet
  - ResNet

## 功能特点

1. 多模型支持
   - EfficientNet：高效的复合缩放网络
   - MobileNet：轻量级移动端优化网络
   - ResNet：深度残差学习网络

2. 实时识别
   - 支持图片实时上传
   - 毫秒级响应
   - 多模型并行预测

3. 可视化展示
   - 支持多种展示方式（图表、饼图、表格）
   - 直观的预测结果对比
   - 详细的概率分布展示

4. 用户友好
   - 响应式设计
   - 直观的操作界面
   - 优雅的交互动效

## 项目亮点

1. 技术创新
   - 采用 Vue 3 最新特性
   - 组件化设计，高度可复用
   - 优雅的状态管理

2. 性能优化
   - 路由懒加载
   - 组件按需加载
   - 图片优化处理

3. 用户体验
   - 流畅的动画效果
   - 友好的错误提示
   - 完善的加载状态

4. 代码质量
   - 统一的代码风格
   - 清晰的项目结构
   - 详细的注释文档

## 使用方式

1. 安装依赖
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
