import '../src/assets/main.css'
import 'primeicons/primeicons.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import VueApexCharts from 'vue3-apexcharts'

import App from './App.vue'
import router from './router'
import { useKakao } from 'vue3-kakao-maps';

const apiKey = import.meta.env.VITE_APP_API_KEY

useKakao(apiKey, ['clusterer', 'services', 'drawing'])

const app = createApp(App)

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
app.use(VueApexCharts);
app.use(pinia)
app.use(router)

app.mount('#app')
