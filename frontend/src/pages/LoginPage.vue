<template>
  <div class="login-wrap">
    <el-card class="card">
      <h2>智能检测平台登录</h2>
      <el-form>
        <el-form-item><el-input placeholder="用户名" v-model="form.username" /></el-form-item>
        <el-form-item><el-input type="password" placeholder="密码" v-model="form.password" /></el-form-item>
        <el-button type="primary" class="btn" @click="go">登录</el-button>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const form = reactive({ username: 'admin', password: '' })
const go = () => router.push('/dashboard')
</script>

<style scoped>
.login-wrap { min-height: 100vh; display: grid; place-items: center; background: linear-gradient(130deg, #dbeafe, #f5d0fe); }
.card { width: 360px; border-radius: 18px; }
.btn { width: 100%; }
</style>
