<template>
  <div>
    <div id="chart" v-if="series.length > 0">
      <!-- ApexCharts 컴포넌트 렌더링 -->
      <apexchart type="bar" height="350" :options="chartOptions" :series="series"></apexchart>
    </div>
    <div v-else>
      <!-- 데이터 로드 중 표시 -->
      <p>Loading chart data...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import VueApexCharts from 'vue3-apexcharts';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { storeToRefs } from 'pinia';

const router = useRouter();
const store = useUserStore();

const url = store.url;
const userPK = ref(store.userPK);
const token = ref(store.token);

const myProducts = ref([]); // 초기값을 빈 배열로 설정
const product_names = ref([]);
const interest_rates = ref([]);
const my_interest_rates = ref([]);
const prime_interest_rates = ref([]);

const series = ref([]); // 차트 데이터 초기화
const chartOptions = ref({}); // 차트 옵션 초기화

onMounted(() => {
  store.getUserInfo();
  getMyProduct();
});

// API 호출 함수
const getMyProduct = async () => {
  try {
    const res = await axios({
      method: 'get',
      url: `${url}/bank_products/products_joined/${userPK.value}/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
    });

    myProducts.value = res.data;

    // 데이터 매핑 후 차트 업데이트
    product_names.value = myProducts.value.map((product) => product.product.product_name);
    interest_rates.value = myProducts.value.map((product) => product.product.interest_rate);
    my_interest_rates.value = myProducts.value.map((product) => product.interest_rate);
    prime_interest_rates.value = myProducts.value.map((product) => product.product.prime_interest_rate);

    updateChart(); // 차트 데이터 업데이트 함수 호출
  } catch (err) {
    console.error(err);
  }
};

// 차트 데이터 및 옵션 업데이트 함수
const updateChart = () => {
  series.value = [
    {
      name: '기준 금리',
      data: interest_rates.value,
    },
    {
      name: '적용 금리',
      data: my_interest_rates.value,
    },
    {
      name: '우대 금리',
      data: prime_interest_rates.value,
    },
  ];

  chartOptions.value = {
    chart: {
      type: 'bar',
      height: 350,
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        endingShape: 'rounded',
      },
    },
    dataLabels: {
      enabled: false,
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent'],
    },
    xaxis: {
      categories: product_names.value, // x축 카테고리 설정
    },
    yaxis: {
      title: {
        text: '단위 : %',
      },
    },
    fill: {
      opacity: 1,
    },
    tooltip: {
      y: {
        formatter(val) {
          return val + '%';
        },
      },
    },
    colors: ['#bebebe', '#FF6708','#bebebe'],
  };
};
</script>

<style scoped>

</style>