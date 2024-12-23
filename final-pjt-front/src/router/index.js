import App from '@/App.vue'
import HomeView from '@/views/HomeView.vue'
import CommunityView from '@/views/CommunityView.vue'
import MapView from '@/views/MapView.vue'
import { createRouter, createWebHistory } from 'vue-router'
import RecommendView from '@/views/RecommendView.vue'
import LoginView from '@/views/LoginView.vue'
import CreatePostView from '@/views/CreatePostView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import UpdatePostView from '@/views/UpdatePostView.vue'
import UpdateUser from '@/components/UpdateUser.vue'
import RecommendDetail from '@/views/RecommendDetailView.vue'


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
      path: '/community/:postId',
      name: 'postdetail',
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
      path: '/recommend/:category/:productId',
      name: 'recommendDetail',
      component: RecommendDetail
    },
    {
      path: '/createPost',
      name: 'createPost',
      component: CreatePostView
    },
    {
      path: '/updatePost/:postId',
      name: 'updatePost',
      component: UpdatePostView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path:'/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path:'/exchange',
      name:'exchange',
      component: ExchangeView,
    },
    {
      path:'/profile/:userId',
      name:'profile',
      component:ProfileView,
    },
    {
      path:'/update-user',
      name:'update-user',
      component:UpdateUser
    }

  ],
})

export default router