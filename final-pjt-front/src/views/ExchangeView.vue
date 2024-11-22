<template>
    <div class="exchange-rate">
        <h2>환율 계산기</h2>
        <div class="exchange-rate-box">
            <div class="box">
                <div class="input-box">
                    <label for="cur-nm">통화 선택</label>
                    <select name="cur-nm" id="cur-nm" v-model="selectedCurrency">
                        <option value="" disabled selected>국가명 통화명</option>
                        <option v-for="country in exchangeInfo" :key="country.id" :value="country">
                            {{ country.cur_nm }}
                        </option>
                    </select>
                </div>
                <div class="input-box">
                    <label for="">금액</label>
                    <input type="number" placeholder="계산할 금액을 입력하세요" v-model="price">
                </div>
            </div>

            <div class="exchange-krw">
                <p>KRW</p>
                <p>{{ calculatedAmount }}원</p>
            </div>
        </div>

        <br>

        <p>환율 그래프</p>
        <div class="chart">
            <ExchangeChart 
            v-for="info in exchangeInfo"
            :key="info.cur_unit"
            :name="info.cur_nm"
            :currency="info.cur_unit"
            width="450"
            style="display: inline-block;"
            elevation="5"
            />
        </div>
    </div>
</template>

<script setup>
import ExchangeChart from '@/components/ExchangeChart.vue';
import axios from 'axios'
import { ref, onMounted, watch } from 'vue'

const price = ref('')
const selectedCurrency = ref('')
const calculatedAmount = ref('')
let cachedExchangeInfo = null
// const exchangeInfo = ref([])
const exchangeInfo = ref([])


// price 값이 변경될 때마다 실행되는 watch 함수
watch(price, (newPrice) => {
  if (newPrice && !selectedCurrency.value) {
    alert('통화명을 먼저 선택해주세요.')
    price.value = '' // 입력된 금액을 초기화합니다

  }
})

// price나 selectedCurrency가 변경될 때마다 계산
watch([price, selectedCurrency], ([newPrice, newCurrency]) => {
    if (!newPrice || !newCurrency) {
        calculatedAmount.value = ''
        return
    }

    try {
        const rateStr = String(newCurrency.deal_bas_r).replace(/,/g, '')
        const rate = parseFloat(rateStr)
        const amount = parseFloat(newPrice) * rate

        if (!isNaN(amount)) {
            calculatedAmount.value = new Intl.NumberFormat('ko-KR', {
                style: 'currency',
                currency: 'KRW'
            }).format(amount)
        } else {
            calculatedAmount.value = ''
        }
    } catch (error) {
        console.error('환율 계산 중 오류 발생:', error)
        calculatedAmount.value = ''
    }
}, { immediate: true })

// 환율 정보 불러오기 함수
const getInfo = function () {
    if (cachedExchangeInfo) {
        exchangeInfo.value = cachedExchangeInfo
        console.log(exchangeInfo.value)
        return
    }

    axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/exchange/'
    })
        .then((res) => {
            exchangeInfo.value = res.data
            cachedExchangeInfo = res.data
            console.log(exchangeInfo.value)
        })
        .catch((err) => {
            console.error("Error fetching data:", err.message)
        })
}

onMounted(() => {
    getInfo()
    console.log(exchangeInfo.value)
})
</script>

<style scoped>
.exchange-rate {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.box { 
    display: flex;
}

.exchange-rate-box {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.exchange-rate h2 {
    margin: 100px auto 30px;
    color: #ff6708;
}

.exchange-rate-box {
    width: 80%;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1);
}

.exchange-rate-box form {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.input-box {
    flex-grow: 1;
}

.input-box,
.exchange-krw {
    position: relative;
    padding: 0 5px;
}

.input-box label,
.exchange-krw p:first-child {
    position: absolute;
    top: -11px;
    left: 11px;
    padding: 0 5px;
    font-size: 14px;
    background-color: #fff;
}

.input-box select,
.input-box input {
    width: 100%;
    padding: 8px 10px;
    border: 1px solid #BCBCBC;
    border-radius: 5px;
}

.input-box select:focus {
    outline: none;
}

.exchange-rate-box button {
    padding: 8px 10px;
    border-radius: 5px;
    color: #fff;
    background-color: #FFB07E;
    border: none;
    cursor: pointer;
    margin-left: 10px;
}

.exchange-krw p:last-child {
    margin-top: 15px;
    padding: 8px 10px;
    border: 1px solid #BCBCBC;
    border-radius: 5px;
}

.chart {
    margin: 20px;
    width: 90%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
}
</style>