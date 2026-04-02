<template>
  <div>
    <h2>图片检测</h2>
    <el-upload drag action="#" :auto-upload="false">
      <el-icon><Plus /></el-icon>
      <div>拖拽或点击上传图片</div>
    </el-upload>
    <el-button type="primary" style="margin-top: 16px">开始检测</el-button>
  </div>
</template>

<script setup>
import { Plus } from '@element-plus/icons-vue'
</script>
