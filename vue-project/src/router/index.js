import App from '@/App.vue'
import HomeView from '@/views/HomeView.vue'
import CommunityView from '@/views/CommunityView.vue'
import MapView from '@/views/MapView.vue'
import { createRouter, createWebHistory } from 'vue-router'
import RecommendView from '@/views/RecommendView.vue'
import LoginView from '@/views/LoginView.vue'
import CreatePost from '@/components/CreatePost.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: RecommendView
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
    },
    {
      path: '/recommend',
      name: 'recommend',
      component: RecommendView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/createpost',
      name: 'createpost',
      component: CreatePost,
    }
  ],
})

export default router
