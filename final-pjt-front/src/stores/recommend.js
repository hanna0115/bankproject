import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useUserStore } from "./user";

export const useRecommendStore = defineStore("recommend", () => {
  const API_URL = 'http://127.0.0.1:8000';
  const userStore = useUserStore()
  const depositProducts = ref([])
  const savingsProducts = ref([])

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
        console.log(res)
        depositProducts.value = res.data.deposit_products
        savingsProducts.value = res.data.savings_products
      })
      .catch(err => console.log('예적금 상품 목록 조회 실패', err))
  }
  return { getProduct, depositProducts, savingsProducts };
});