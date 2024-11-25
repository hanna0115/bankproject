<template>
  <nav class="nav">
    <RouterLink :to="{name:'home'}" class="logo">ORANGE SALADA</RouterLink>
    <div class="real-nav">
      <RouterLink :to="{name:'recommend'}">금융상품추천</RouterLink>
      <RouterLink :to="{name:'map'}">지도</RouterLink>
      <RouterLink :to="{name:'community'}">커뮤니티</RouterLink>
      <RouterLink :to="{name:'exchange'}">환율 계산기</RouterLink>
    </div>

    <div class="is-logged-in" v-if="store.isLoggedIn">
      <button @click="router.push({ name: 'profile', params: { userId: store.userPK }})">
        <i class="pi pi-user user-icon"></i>
      </button>
      <button @click="store.logOut" class="logout-btn">
      로그아웃
      </button>
    </div>

  <RouterLink
  v-else
  :to="{name: 'login'}" class="login-btn">로그인</RouterLink>
 
  </nav>
</template>

<script setup>
import { onMounted } from 'vue'
import { gsap } from 'gsap'
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user';
import { useRoute } from 'vue-router';

const router = useRouter()
const store = useUserStore()

onMounted(() => {
  // Homepage container animation
  gsap.fromTo(".recommendation-container",
    { opacity: 0, y: -50 },
    { opacity: 1, y: 0, duration: 1, ease: "power2.out" }
  );
  
  // Navbar animation with timing sync
  const stagger = 0.6;
  const totalProducts = 5;
  const productAnimationDuration = 3;
  const totalDelay = (totalProducts * stagger + productAnimationDuration);
  
  gsap.fromTo(".nav",
    { opacity: 0, y: -50 },
    { 
      opacity: 1, 
      y: 0, 
      duration: 1,
      delay: 0.2,
      ease: "power2.out"
    }
  );
});
</script>

<style scoped>
.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1280px;
  min-width: 900px;
  margin: 0 auto;
  padding: 10px 20px;
}

.logo {
  font-size: 30px;
  color: #FF6709;
  font-weight: bold;
  font-style: italic;
}

.real-nav {
  display: flex;
  position: relative;
  top: 6px;
  right: 75px;
}

.real-nav a {
  padding: 12px 20px;
  color: #B9B9B9;
  font-size: 18px;
  font-weight: 500;
}

.user-icon {
  cursor: pointer;
  padding: 10px;
  color: white;
  background-color: rgba(255, 103, 8, 0.6);
  border-radius: 50%;
  height: 32px;
  width: 35px;
  margin-right: 5px;
}

/* .user-btn {
  margin-top: 10px;
} */

.login-btn,
.logout-btn {
  background-color: rgba(255, 103, 8, 0.6);
  color: white;
  padding: 5px 12px;
  border-radius: 30px;
  width: 83px;
  font-size: 13px;
  width: 83px;
  height: 29px;
  text-align: center;
  margin-top: 10px;
}

button.login-btn {
  border: none;
  cursor: pointer;
  padding: 5px 12px;
  font-size: 13px;
  width: 83px;
  height: 29px;
  margin-top: 10px;
}
</style>