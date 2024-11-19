import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useCounterStore = defineStore("counter", () => {
  const API_KEY = "4k9NI9akiSV3cvGuiiqpCQPaRLtactZc";
  const URL = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON";

  const exchanges = ref([]);

  const exchangeInfo = () => {
    axios({
      method: "get",
      url: URL,
      params: {
        authkey: API_KEY,
        searchdate: "20241118",
        data: "AP01",
      },
    }).then((response) => {
      exchanges.value = response.data;
      console.log(response.data);
    });
  };
  return { exchangeInfo, exchanges };
});
