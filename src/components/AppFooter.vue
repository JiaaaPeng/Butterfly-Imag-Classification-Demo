<template>
  <footer class="app-footer">
    <div class="footer-content">
      <div class="footer-section">
        <h3>关于我们</h3>
        <p>致力于为用户提供最先进的图像识别解决方案</p>
      </div>
      <div class="footer-section">
        <h3>联系方式</h3>
        <p>邮箱：contact@example.com</p>
        <p>电话：(+86) 123-4567-8900</p>
      </div>
      <div class="footer-section">
        <h3>关注我们</h3>
        <div class="social-links">
          <el-button type="primary" circle
            ><el-icon><Platform /></el-icon
          ></el-button>
          <el-button type="primary" circle
            ><el-icon><Share /></el-icon
          ></el-button>
          <el-button type="primary" circle
            ><el-icon><Connection /></el-icon
          ></el-button>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2024 图像识别系统. All rights reserved.</p>
    </div>
  </footer>
</template>

<script setup>
import { Platform, Share, Connection } from "@element-plus/icons-vue";
</script>

<style scoped>
.app-footer {
  background-color: #2c3e50;
  color: #ffffff;
  padding: 40px 0 20px;
  margin-top: auto;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
  padding: 0 20px;
}

.footer-section h3 {
  color: #ffffff;
  margin-bottom: 20px;
  font-size: 1.2em;
}

.footer-section p {
  color: #b3b3b3;
  line-height: 1.6;
}

.social-links {
  display: flex;
  gap: 15px;
  margin-top: 15px;
}

.footer-bottom {
  text-align: center;
  margin-top: 40px;
  padding-top: 20px;
  border-top: 1px solid #3a4b5f;
}

.footer-bottom p {
  color: #b3b3b3;
  font-size: 0.9em;
}

@media (max-width: 768px) {
  .footer-content {
    grid-template-columns: 1fr;
    gap: 30px;
  }
}
</style> 