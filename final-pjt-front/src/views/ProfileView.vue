<template>
    <div class="container">
        <h2 class="title">마이 페이지</h2>
        
        <div class="content" v-if="store.user">
            <div>
                <p class="user-name"><span class="user-realname">{{ store.user.name }}</span class="nim">님</p>
                <button class="modify-btn" @click="router.push('/update-user')">내 정보 수정</button>
            </div>
            <div class="product">
                <span>내가 가입한 예적금 상품</span>
    
                <button class="product-btn" @click="connectMyProduct">연동 하기</button>
            </div>
        </div>
        <ProductIItem 
        v-for="(myProduct, index) in myProducts"
        :key="myProduct.pk"
        :my-product="myProduct"
        :index="index"
        />

        <br>
        <div class="chart">
            차트 한 번 그려 봄
            <ProfileChart />
        </div>
    </div>
</template>

<script setup>

import ProductIItem from '@/components/ProductIItem.vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';
import ProfileChart from '@/components/ProfileChart.vue';
import { onMounted, ref } from 'vue';
import axios from 'axios';
import { storeToRefs } from 'pinia';

const router = useRouter()
const store = useUserStore()


const url = store.url
// const { userPK, token } = storeToRefs(useUserStore)
const userPK = ref(store.userPK)
const token = ref(store.token)

const myProducts = ref(null)

onMounted(() => {
    store.getUserInfo()
    getMyProduct()
})

// 1. 연동된 경우, 바로 조회
const getMyProduct = () => {
    axios({
        method:'get',
        url:`${url}/bank_products/products_joined/${userPK.value}/`,
        headers:{
            Authorization:`Token ${token.value}`
        }
    })
    .then((res) => {
        myProducts.value = res.data
        console.log('조회요청함')
        console.log(res.data)
    })
    .catch((err) => console.log(err, userPK.value, token.value))
}


// 2. 연동하기
const connectMyProduct = () => {

    axios({
        method:'post',
        url:`${url}/bank_products/products_joined/${userPK.value}/`,
        headers:{
            Authorization:`Token ${token.value}`
        }
    })
    .then((res) => {
        myProducts.value = res.data.data
    })
    .catch((err) => console.log(err, userPK.value, token.value))
}



</script>


<style scoped>
.container {
    display: flex;
    flex-direction: column;
    width: 60%;
    margin: 0 auto;
    margin-top: 100px;
}

/* .content {
    margin-left: 180px;
} */

.title {
    margin: 0 auto;
    margin-bottom: 20px;
    color: #FF6708;
}

.user-name {
    display: flex;
    justify-content: left;
    font-size: 20px;
    color: #bebebe;
    font-weight: 700;
}

.user-realname {
    color: #FFA46B;
    font-weight: 700;
    margin-right: 5px;

}

.modify-btn {
    background-color: #FF6708;
    color: white;
    border-radius: 20px;
    padding: 0 8px;
    margin-top: 10px;
    margin-bottom: 30px;
    cursor: pointer;
}

.product {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

.product > span {
    font-size: 18px;
    font-weight: 700;
    color: #808080;
}

.product > button {
    font-size: 12px;
    /* margin-right: 250px ; */
    background-color: #FF6708;
    color: white;
    padding: 0 8px;
    border-radius: 20px;
    cursor: pointer;
}

.product-content {
    display: flex;
}

.product-content > p {
    color: #FFA46B;
    font-size: 19px;
}

.product-content > span {
    margin-left: 37px;
    padding-top: 5px;
}

.product-duration {
    margin-left: 60px;
    font-size: 13px;
    color: #BCBCBC;
}

.duration-section {
    display: flex;
    justify-content: space-between;
}


.duration-section > span {
    margin-right: 253px;
}

.monthly-amount {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
}

.chart {
    text-align: center;
}

</style>