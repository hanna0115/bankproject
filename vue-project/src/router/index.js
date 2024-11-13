import App from '@/App.vue'
import HomeView from '@/views/HomeView.vue'
import CommunityView from '@/views/CommunityView.vue'
import MapView from '@/views/MapView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView,
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    }
  ],
})

export default router
