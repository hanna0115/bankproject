<template>
    <div class="card" v-if="currency !== 'KRW'">
        <v-card-item>
            <div class="text-h6 font-weight-bold mb-1">
                {{ name }}
            </div>
            <img :src="`https://ssl.pstatic.net/imgfinance/chart/marketindex/area/month/FX_${getCurrencyCode(currency)}KRW.png`"
                :alt="`${name} exchange graph`" height="160">
        </v-card-item>

        <v-card-actions>
            <v-btn ariant="tonal" color="#1089FF" class="ml-auto"
                :href="`https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_${currency}KRW`">
            </v-btn>
        </v-card-actions>

    </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
    name: String,
    currency: String
});

const getCurrencyCode = computed(() => {
    const mapping = {
        'CNH': 'CNY',
        'JPY(100)': 'JPY',
        'IDR(100)': 'IDR'
    };
    return (cur_unit) => mapping[cur_unit] || cur_unit.split('(')[0];
});
</script>

<style scoped>
.card {
    text-align: center;
    width: 350px;
    transition: 400ms;
    margin: 10px;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1);
}

.card:hover {
    color: #1089FF;
    transform: scale(1.02);
}

img {
    width: 100%;
}
</style>