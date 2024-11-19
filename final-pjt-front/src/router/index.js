import App from '@/App.vue'
import HomeView from '@/views/HomeView.vue'
import CommunityView from '@/views/CommunityView.vue'
import MapView from '@/views/MapView.vue'
import { createRouter, createWebHistory } from 'vue-router'
import RecommendView from '@/views/RecommendView.vue'
import LoginView from '@/views/LoginView.vue'
import CreatePost from '@/components/CreatePost.vue'
import SignUpView from '@/views/SignUpView.vue'
import PostList from '@/components/PostList.vue'
import PostDetail from '@/components/PostDetail.vue'
import RecommendDetail from '@/components/RecommendDetail.vue'
import ExchangeView from '@/views/ExchangeView.vue'


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
    },
    {
      path:'/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path:'/postlist',
      name:'postlist',
      component: PostList
    },
    {
      path:'/postdetail',
      name:'postdetail',
      component: PostDetail // postlist의 children으로 수정할 것
    },
    {
      path:'/recommend-detail',
      name:'recommenddetail',
      component: RecommendDetail,
    },
    {
      path:'/exchange',
      name:'exchange',
      component: ExchangeView,
    }
  ],
})

export default router
