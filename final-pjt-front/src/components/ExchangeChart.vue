<template>
    <div>
        {{ exchangeInfo }}
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'

// 캐시된 환율 정보를 저장할 변수 (여러 컴포넌트에서 공유 가능)
let cachedExchangeInfo = null

const exchangeInfo = ref([])

// 환율 정보 불러오기 함수
const getInfo = function() {
    // 캐시된 데이터가 있으면 서버에 요청하지 않고 캐시된 데이터를 사용
    if (cachedExchangeInfo) {
        exchangeInfo.value = cachedExchangeInfo;
        console.log("Using cached data:", exchangeInfo.value)
        return
    }

    // 서버에 요청하여 환율 정보를 가져옴
    axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/exchange/'
    })
    .then((res) => {
        exchangeInfo.value = res.data
        cachedExchangeInfo = res.data  // 데이터를 캐시에 저장
        console.log("Fetched data from server:", exchangeInfo.value)
    })
    .catch((err) => {
        console.error("Error fetching data:", err.message)
    });
}

// 컴포넌트가 마운트될 때 환율 정보를 불러옴
onMounted(() => {
    getInfo()
})


</script>

<style scoped>

</style>