<template>
    <div class="recommendation-container">
      <h2 class="recommendation-badge">예적금 상품 추천</h2>
      <div class="account-toggle">
        <div class="toggle-slider" :style="sliderStyle"></div>
        <button @click="setCategory(false)" :class="{ active: !category }" class="toggle-button">예금</button>
        <button @click="setCategory(true)" :class="{ active: category }" class="toggle-button">적금</button>
      </div>
      <p class="recommendation-intro" v-if="userStore.isLoggedIn && userStore.user"><span>{{ userStore.user.name }}</span>님의 목표 달성에 도움이 되는</p>
      <p class="recommendation-intro" v-else><span>가장 많은 사람들</span>이 가입한</p>
      <p class="recommendation-title">금융상품 Best 5!</p>
      <div class="product-list">
        <div v-for="(product, index) in category ? recommendStore.savingsProducts : recommendStore.depositProducts"
          :key="product.id" class="product-item">
          <RouterLink :to="{ name: 'recommendDetail', params: { category: category ? 'savings' : 'deposit', productId: product.id } }">
            <div class="product-card">
              <div class="product-card-inner">
                <div class="product-card-front">
                  <div class="product-content">
                    <span class="product-number">{{ index + 1 }}</span>
                    <img class="product-icon" :src="getBankLogo(product.company_name)" alt="Product Icon">
                    <div class="product-info">
                      <p class="product-name">{{ product.company_name }}</p>
                      <p class="product-detail">{{ product.product_name }}</p>
                    </div>
                    <div class="product-rate">
                      <p class="rate-label">최고</p>
                      <p class="rate-value">{{ product.prime_interest_rate }}%</p>
                      <p class="rate-condition">기본 {{ product.interest_rate }}%</p>
                    </div>
                  </div>
                </div>
                <div class="product-card-back"></div>
              </div>
            </div>
          </RouterLink>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { onMounted, ref, computed } from 'vue';
  import { gsap } from 'gsap';
  import { useUserStore } from '@/stores/user';
  import { useRecommendStore } from '@/stores/recommend';
  
  const userStore = useUserStore();
  const recommendStore = useRecommendStore();
  const category = ref(false); // false는 예금, true는 적금
  
  const setCategory = (value) => {
    category.value = value;
  };
  
  const sliderStyle = computed(() => ({
    transform: category.value ? 'translateX(100%)' : 'translateX(0)'
  }));
  
  const getBankLogo = (categoryName) => {
    const bankName = categoryName.split(' > ').pop();
    const bankLogos = {
      'KB국민은행': 'src/assets/images/kb.png',
      '신한은행': 'src/assets/images/shinhan.png',
      '하나은행': 'src/assets/images/hana.png',
      '우리은행': 'src/assets/images/woori.png',
      'NH농협은행': 'src/assets/images/nh.png',
      'IBK기업은행': 'src/assets/images/IBK.png',
      'KDB산업은행': 'src/assets/images/KDB.png',
      'SC제일은행': 'src/assets/images/sc.png',
      '부산은행': 'src/assets/images/BUSAN.png',
      'iM뱅크': 'src/assets/images/IM.png',
      'SH수협은행': 'src/assets/images/SH.png',
      '경남은행': 'src/assets/images/BUSAN.png',
      '카카오뱅크': 'src/assets/images/kakao.png',
      '광주은행': 'src/assets/images/KWANGJU.png',
      '토스뱅크': 'src/assets/images/toss.png',
      '전북은행': 'src/assets/images/JEONBUK.png',
      '케이뱅크': 'src/assets/images/kbank.png',
      '제주은행': 'src/assets/images/shinhan.png',
    };
    return bankLogos[bankName] || '/images/default.png';
  };
  
  onMounted(() => {
    recommendStore.getProduct();
    const productItems = document.querySelectorAll('.product-item');
    
    gsap.fromTo(".recommendation-container", 
      { opacity: 0, y: -50 }, 
      { 
        opacity: 1, 
        y: 0, 
        duration: 1, 
        delay: 0.8,
        ease: "power2.out",
        onComplete: () => {
          productItems.forEach((item, index) => {
            const card = item.querySelector('.product-card-inner');
            let isAnimating = true;
            const animationDelay = index * 0.6;
            const animationDuration = 3;
            const totalAnimationTime = (animationDelay + animationDuration) * 1000;
            
            setTimeout(() => {
              isAnimating = false;
            }, totalAnimationTime);
            
            item.addEventListener('mouseenter', () => {
              if (!isAnimating) {
                card.style.animation = 'none';
                item.classList.add('hover-effect');
              }
            });
            
            item.addEventListener('mouseleave', () => {
              if (!isAnimating) {
                item.classList.remove('hover-effect');
              }
            });
          });
        }
      }
    );
  });
  </script>
  
  <style scoped>
  .recommendation-container {
  margin: 100px auto;
  text-align: center;
}

.recommendation-badge {
  margin-bottom: 20px;
  font-size: 30px;
  font-weight: 700;
  color: #FF6708;
}

.account-toggle {
  display: inline-flex;
  background-color: #f0f0f0;
  border-radius: 30px;
  padding: 4px;
  margin-bottom: 20px;
  position: relative;
  overflow: hidden;
}

.toggle-slider {
  position: absolute;
  top: 4px;
  left: 4px;
  width: calc(50% - 4px);
  height: calc(100% - 8px);
  background-color: #fff;
  border-radius: 25px;
  transition: transform 0.3s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.toggle-button {
  border: none;
  background-color: transparent;
  padding: 3px 10px;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 14px;
  font-weight: 500;
  position: relative;
  z-index: 1;
}

.toggle-button.active {
  color: #333;
}

.toggle-button:focus {
  outline: none;
}

.toggle-button:hover:not(.active) {
  background-color: rgba(255, 255, 255, 0.5);
}

.recommendation-intro, .recommendation-title {
  margin-top: 8px;
  font-size: 20px;
  font-weight: 500;
  color: #ABABAB;
}

.recommendation-intro > span {
  color: #FF6708;
  font-weight: 700;
}

.recommendation-title {
  margin-top: 8px;
}

.product-list {
  margin-top: 50px;
}

.product-item {
  width: 650px;
  height: 100px;
  margin: 10px auto;
  perspective: 1000px;
  cursor: pointer;
}

.product-card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: all 0.3s ease;
}

.product-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: all 0.3s ease;
  transform-style: preserve-3d;
}

.product-card-front, .product-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 15px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.2);
}

.product-card-front {
  background-color: white;
  transition: all 0.3s ease;
}

.product-card-back {
  background-color: #fffdfd;
  transform: rotateX(180deg);
}

/* 호버 효과 */
.product-item:hover .product-card {
  transform: scale(1.05);
}

/* 클릭 효과 */
.product-item:active .product-card {
  transform: scale(0.95);
}

.hover-effect .product-card-front {
  background-color: #FFB07E;
}

.product-content {
  display: flex;
  align-items: center;
  padding: 0 20px;
  width: 100%;
}

.product-number {
  font-size: 24px;
  font-weight: bold;
  margin-right: 20px;
}

.product-icon {
  width: 40px;
  height: 40px;
}

.product-info {
  flex-grow: 1;
  text-align: center;
}

.product-name {
  font-size: 16px;
  color: #666;
}

.product-detail {
  font-size: 18px;
  font-weight: bold;
}

.product-rate {
  text-align: right;
}

.rate-label {
  font-size: 14px;
}

.rate-value {
  font-size: 24px;
  font-weight: bold;
  color: #FF6708;
}

.rate-condition {
  font-size: 12px;
  color: #999;
}

@keyframes flipCard {
  0% {
    transform: rotateX(0deg);
  }
  100% {
    transform: rotateX(-360deg);
  }
}

.product-item:nth-child(1) .product-card-inner {
  animation: flipCard 3s 1;
  animation-delay: 0s;
}

.product-item:nth-child(2) .product-card-inner {
  animation: flipCard 3s 1;
  animation-delay: 0.6s;
}

.product-item:nth-child(3) .product-card-inner {
  animation: flipCard 3s 1;
  animation-delay: 1.2s;
}

.product-item:nth-child(4) .product-card-inner {
  animation: flipCard 3s 1;
  animation-delay: 1.8s;
}

.product-item:nth-child(5) .product-card-inner {
  animation: flipCard 3s 1;
  animation-delay: 2.4s;
}
  </style>