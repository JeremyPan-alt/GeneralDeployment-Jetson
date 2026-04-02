<template>
  <div>
    <h2>视频检测（双摄像头）</h2>
    <el-row :gutter="16">
      <el-col :span="12"><el-card><p>Camera A（ROI + 3秒停留检测）</p><div class="video"></div></el-card></el-col>
      <el-col :span="12"><el-card><p>Camera B（OCR）</p><div class="video"></div></el-card></el-col>
    </el-row>
    <el-space style="margin-top: 16px">
      <el-button type="primary">启动实时检测</el-button>
      <el-button>停止</el-button>
    </el-space>
  </div>
</template>

<style scoped>
.video { height: 260px; border-radius: 10px; background: repeating-linear-gradient(45deg,#e2e8f0,#e2e8f0 10px,#f8fafc 10px,#f8fafc 20px); }
</style>
