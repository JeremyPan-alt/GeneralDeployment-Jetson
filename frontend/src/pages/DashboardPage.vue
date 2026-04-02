<template>
  <div>
    <h2>运行总览</h2>
    <el-row :gutter="16">
      <el-col :span="6" v-for="item in cards" :key="item.label">
        <el-card>
          <p>{{ item.label }}</p>
          <h3>{{ item.value }}</h3>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
const cards = [
  { label: '在线时长', value: '12d 08h' },
  { label: '今日告警', value: '28' },
  { label: 'OCR成功率', value: '98.1%' },
  { label: '模型延迟', value: '84ms' }
]
</script>
