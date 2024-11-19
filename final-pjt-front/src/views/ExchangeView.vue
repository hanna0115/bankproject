<template>
    <div>
        <button @click="test">환율 정보 가져오기</button>
        <div v-if="store.exchanges.length">
            <div v-for="exchange in store.exchanges" :key="exchange.cur_unit">
                <p>{{ exchange.cur_nm }}: {{ exchange.deal_bas_r }}</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { onMounted } from 'vue';

const store = useCounterStore();

const test = () => {
    store.exchangeInfo();
}

// 컴포넌트가 마운트될 때 자동으로 데이터를 가져오려면 아래 코드 추가
onMounted(() => {
    test();
})
</script>

<style lang="scss" scoped>

</style>