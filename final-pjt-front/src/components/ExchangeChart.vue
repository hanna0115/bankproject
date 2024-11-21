<template>
    <div class="card">
        <v-card-item>
            <div class="text-h6 font-weight-bold mb-1">
            {{ name }}
            </div>
            <img :src="`https://ssl.pstatic.net/imgfinance/chart/marketindex/area/month/FX_${currency}KRW.png`" alt="exchange graph" height="160">
        </v-card-item>

        <v-card-actions>
        <v-btn 
            ariant="tonal"
            color="#1089FF"
            class="ml-auto"
            :href="`https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_${currency}KRW`"
        >
        </v-btn>
        </v-card-actions>

    </div>
</template>

<script setup>
const props = defineProps({
  currency: String,
  name: String,
})

</script>

<style scoped>
.card {
    text-align: center;
    width: 350px;
    transition: 400ms;
    margin: 0 10px;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1);
}
.card:hover {
  color: #1089FF;
  transform: scale(1.02);
}

img {
    width: 80%;
}
</style>