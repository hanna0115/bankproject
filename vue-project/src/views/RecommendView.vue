<template>
    <div class="recommendation-container">
        <span class="recommendation-badge">금융상품 추천</span>
        <p class="recommendation-intro"><span class="user-name">김선명</span>님의 목표 달성에 도움이 되는</p>
        <p class="recommendation-title">금융상품 Best 5!</p>
        <div class="product-list">
            <div v-for="n in 5" :key="n" class="product-item">
                <div class="product-card">
                    <div class="product-card-inner">
                        <div class="product-card-front">
                            <div class="product-content">
                                <span class="product-number">{{ n }}</span>
                                <img class="product-icon" :src="n === 2 ? '/path-to-globe-icon.png' : '/path-to-card-icon.png'" alt="Product Icon">
                                <div class="product-info">
                                    <p class="product-name">웰컴저축은행</p>
                                    <p class="product-detail">웰뱅 위킹 적금</p>
                                </div>
                                <div class="product-rate">
                                    <p class="rate-label">최고</p>
                                    <p class="rate-value">10%</p>
                                    <p class="rate-condition">기본 1%</p>
                                </div>
                            </div>
                        </div>
                        <div class="product-card-back"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { gsap } from 'gsap';

onMounted(() => {
  const productItems = document.querySelectorAll('.product-item');
  
  // 상품 목록 애니메이션
  gsap.fromTo(".recommendation-container",
    { opacity: 0, y: -50 },
    { 
      opacity: 1, 
      y: 0, 
      duration: 1,
      delay: 0.8, // Delay after navbar animation
      ease: "power2.out",
      onComplete: () => {
        // Start product card animations after container appears
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
    display: inline-block;
    background-color: rgba(255, 103, 8, 0.6);
    color: white;
    padding: 5px 12px;
    border-radius: 30px;
    font-size: 13px;
    margin-bottom: 20px;
}

.recommendation-intro {
    margin-top: 8px;
    font-size: 20px;
    font-weight: 700;
    color: #ABABAB;
}

.user-name {
    color: rgba(255, 103, 8, 0.6);
}

.recommendation-title {
    margin-top: 8px;
    font-size: 20px;
    font-weight: 700;
    color: #FFAE17;
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
}

.product-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.3s;
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
    transition: background-color 0.3s ease;
}

.product-card-back {
    background-color: #fffdfd;
    transform: rotateX(180deg);
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
    font-size: 18px;
    font-weight: bold;
}

.product-detail {
    font-size: 16px;
    color: #666;
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
    0% { transform: rotateX(0deg); }
    100% { transform: rotateX(-360deg); }
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