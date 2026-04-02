import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../pages/LoginPage.vue'
import MainLayout from '../layout/MainLayout.vue'
import DashboardPage from '../pages/DashboardPage.vue'
import ImageDetectPage from '../pages/ImageDetectPage.vue'
import VideoDetectPage from '../pages/VideoDetectPage.vue'
import RecordsPage from '../pages/RecordsPage.vue'
import ManualAdjustPage from '../pages/ManualAdjustPage.vue'

const routes = [
  { path: '/login', component: LoginPage },
  {
    path: '/',
    component: MainLayout,
    children: [
      { path: '', redirect: '/dashboard' },
      { path: '/dashboard', component: DashboardPage },
      { path: '/image-detect', component: ImageDetectPage },
      { path: '/video-detect', component: VideoDetectPage },
      { path: '/records', component: RecordsPage },
      { path: '/manual-adjust', component: ManualAdjustPage }
    ]
  }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
