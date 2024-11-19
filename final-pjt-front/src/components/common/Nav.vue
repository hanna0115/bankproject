<template>
  <nav class="nav">
    <RouterLink :to="{name:'home'}" class="logo">BANKPROJECT</RouterLink>
    <div class="real-nav">
      <RouterLink :to="{name:'recommend'}">금융상품추천</RouterLink>
      <RouterLink :to="{name:'map'}">지도</RouterLink>
      <RouterLink :to="{name:'community'}">커뮤니티</RouterLink>
      <RouterLink :to="{name:'exchange'}">환율 계산기</RouterLink>
    </div>
    <RouterLink :to="{name: 'login'}" class="login-btn">로그인</RouterLink>
  </nav>
</template>

<script setup>
import { onMounted } from 'vue'
import { gsap } from 'gsap'
import { RouterLink, RouterView } from 'vue-router'

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
  min-width: 900px;
  padding: 10px 20px;
}

.logo {
  font-size: 30px;
  color: #FF6709;
  font-weight: bold;
}

.real-nav {
  display: flex;
  position: relative;
  top: 6px;
  right: 75px;
}

.real-nav a {
  padding: 12px;
  color: #B9B9B9;
  font-size: 18px;
  font-weight: bold;
}

.login-btn {
  position: relative;
  background-color: rgba(255, 103, 8, 0.6);
  color: white;
  padding: 5px 12px;
  border-radius: 30px;
  top: 6px;
}
</style>