<template>
  <div>
    <h2>检测记录</h2>
    <el-table :data="rows" stripe>
      <el-table-column prop="id" label="ID" width="80"/>
      <el-table-column prop="detectedObject" label="目标"/>
      <el-table-column prop="ocrText" label="OCR文本"/>
      <el-table-column prop="cameraAt" label="触发时间"/>
      <el-table-column prop="status" label="状态"/>
    </el-table>
  </div>
</template>

<script setup>
const rows = [
  { id: 101, detectedObject: 'person', ocrText: 'AB1234', cameraAt: '2026-04-02 08:16:09', status: '已确认' },
  { id: 102, detectedObject: 'truck', ocrText: '粤B-9C82', cameraAt: '2026-04-02 08:19:42', status: '待复核' }
]
</script>
