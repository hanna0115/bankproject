import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useUserStore } from "./user";

export const useRecommendStore = defineStore("recommend", () => {
  const API_URL = 'http://127.0.0.1:8000';
  const userStore = useUserStore()
  const depositProducts = ref([])
  const savingsProducts = ref([])

  // 1. 저금 목표에 가장 잘 맞는 상품 가져오기
  const getProduct = function () {
    const params = userStore.isLoggedIn ? userStore.user.saving_purpose : []
    axios({
      method: 'get',
      url: `${API_URL}/bank_products/products_recommend/`,
      params: {
        saving_purpose: JSON.stringify(params)
      }
    })
      .then(res => {
        depositProducts.value = res.data.deposit_products
        savingsProducts.value = res.data.savings_products
      })
      .catch(err => console.log('예적금 상품 목록 조회 실패', err))
  }


  // 2. 상품 상세 정보 가져오기
  const product = ref({}); // 초기화

  const getProductDetail = function (category, productId) {
      console.log(depositProducts)
      // 카테고리에 따라 적절한 상품 목록에서 해당 상품을 찾습니다.
      if (category === 'deposit') {
          const foundProduct = depositProducts.find(p => p.id === productId);
          if (foundProduct) {
              product.value = foundProduct; // 상품이 발견되면 설정
          } else {
              console.error(`상품 ID ${productId}를 찾을 수 없습니다.`);
          }
      } else {
          const foundProduct = savingsProducts.find(p => p.id === productId);
          if (foundProduct) {
              product.value = foundProduct; // 상품이 발견되면 설정
          } else {
              console.error(`상품 ID ${productId}를 찾을 수 없습니다.`);
          }
      }
  };

  return { getProduct, depositProducts, savingsProducts, getProductDetail, product };
});