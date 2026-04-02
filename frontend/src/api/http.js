import axios from 'axios'

export const http = axios.create({
  baseURL: import.meta.env.VITE_BACKEND_URL || 'http://127.0.0.1:8000/api',
  timeout: 5000
})
