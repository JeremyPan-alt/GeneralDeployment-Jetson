<template>
  <div>
    <h2>手动调整</h2>
    <el-form label-width="120px" class="form">
      <el-form-item label="记录ID"><el-input v-model="form.id"/></el-form-item>
      <el-form-item label="目标类别"><el-input v-model="form.detectedObject"/></el-form-item>
      <el-form-item label="OCR结果"><el-input v-model="form.ocrText"/></el-form-item>
      <el-form-item label="备注"><el-input type="textarea" v-model="form.remark"/></el-form-item>
      <el-space>
        <el-button type="primary">保存修改</el-button>
        <el-button type="danger">删除记录</el-button>
        <el-button>新增一条</el-button>
      </el-space>
    </el-form>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
const form = reactive({ id: '', detectedObject: '', ocrText: '', remark: '' })
</script>

<style scoped>
.form { max-width: 760px; }
</style>
