<template>
  <div>
    <Bar :data="chartData" :options="chartOptions" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';

// Chart.js 모듈 등록
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

// 차트 데이터 및 옵션 정의
const chartData = ref({
  labels: ['January', 'February', 'March'],
  datasets: [
    {
      label: 'Sales',
      backgroundColor: '#42A5F5',
      data: [40, 20, 12],
    },
  ],
});

const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      beginAtZero: true,
    },
  },
});

// 컴포넌트가 마운트될 때 실행되는 로직
onMounted(() => {
  console.log('Bar chart loaded');
});
</script>

<style scoped>
/* 차트 크기를 조정하기 위한 스타일 */
div {
  width: 100%;
  height: 400px;
}
</style>