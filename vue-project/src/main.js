import '../src/assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import { useKakao } from 'vue3-kakao-maps';

useKakao('b58d7d3c1cb707eebc5096f6365a6285', ['clusterer', 'services', 'drawing'])

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
