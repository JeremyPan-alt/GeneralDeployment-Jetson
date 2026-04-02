<template>
  <div class="shell">
    <aside class="sidebar">
      <h2>Jetson Vision</h2>
      <el-menu :default-active="active" router class="menu">
        <el-menu-item index="/dashboard">总览</el-menu-item>
        <el-menu-item index="/image-detect">图片检测</el-menu-item>
        <el-menu-item index="/video-detect">视频检测</el-menu-item>
        <el-menu-item index="/records">检测记录</el-menu-item>
        <el-menu-item index="/manual-adjust">手动调整</el-menu-item>
      </el-menu>
    </aside>
    <main class="main">
      <header>
        <el-input placeholder="搜索记录 / 目标 / OCR" class="search" />
        <el-tag type="success">7x24 在线</el-tag>
      </header>
      <section class="content">
        <router-view />
      </section>
    </main>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const active = computed(() => route.path)
</script>

<style scoped>
.shell { display: grid; grid-template-columns: 240px 1fr; min-height: 100vh; }
.sidebar { background: #f8fafc; border-right: 1px solid #e2e8f0; padding: 20px; }
.menu { border: none; background: transparent; }
.main { padding: 20px; }
header { display: flex; justify-content: space-between; margin-bottom: 16px; }
.search { width: 320px; }
.content { background: #fff; border-radius: 16px; padding: 20px; min-height: 85vh; box-shadow: 0 16px 40px rgba(15, 23, 42, .06); }
</style>
