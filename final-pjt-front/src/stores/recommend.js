import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useRecommendStore = defineStore("recommend", () => {
  const API_URL = 'http://127.0.0.1:8000';
  const depositProducts = ref([])
  const savingsProducts = ref([])

  const getProduct = function () {
    axios({
      method: 'get',
      url: `${API_URL}/bank_products/products_recommend/`
    })
      .then(res => {
        console.log(res.data)
        depositProducts.value = res.data.deposit_products
        savingsProducts.value = res.data.savings_products
      })
      .catch(err => console.log('예적금 상품 목록 조회 실패', err))
  }
  return { getProduct, depositProducts, savingsProducts };
});