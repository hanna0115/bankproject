<template>
  <nav class="nav">
    <!-- 로고에 애니메이션 적용 -->
    <RouterLink :to="{name:'home'}" class="logo">BANKPROJECT</RouterLink>
    <div class="real-nav">
      <RouterLink :to="{name:'recommend'}">금융상품추천</RouterLink>
      <RouterLink :to="{name:'map'}">지도</RouterLink>
      <RouterLink :to="{name:'community'}">커뮤니티</RouterLink>
    </div>
    <RouterLink :to="{name: 'login'}" class="login-btn">로그인</RouterLink>
  </nav>

  <RouterView />
</template>

<script setup>
import { onMounted } from 'vue'
import { gsap } from 'gsap'
import { RouterLink, RouterView } from 'vue-router'

onMounted(() => {
  // 페이지가 로드될 때 로고에 애니메이션 적용
  gsap.fromTo(".logo", 
    { opacity: 0, y: -50 },  // 초기 상태 (투명하고 위쪽에 위치)
    { opacity: 1, y: 0, duration: 1, ease: "power2.out" } // 최종 상태 (보이고 제자리로 이동)
  );
});
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  color: #333;
}

a {
  text-decoration: none;
}

.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: clamp(1232px, calc((100vw - 1752px)*((1376 - 1232) /(2560 - 1752)) + 1232px), 1376px);
  margin: auto;
  /* border: 1px solid black; */
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

  /* gap:50px; */

}

.real-nav a {
  padding: 12px;
  color: #B9B9B9;
  font-size: 18px;
  font-weight:bold;
}

.login-btn {
  position: relative;
  background-color: rgba(255,103,8,0.6);
  color: white;
  padding: 5px 12px; 
  border-radius: 30px;
  top: 6px;
}
</style>