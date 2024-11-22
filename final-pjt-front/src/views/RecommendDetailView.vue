<template>
    <div class="container">
        <div class="product-container">
            <div class="product-info"> <!-- 상품 정보-->
                <h2 class="product-title">{{ product.product_name }}</h2>
                <p class="bank-name">{{ product.company_name }}</p>
                <div class="product-event" v-if="product.events">
                    <span v-for="event in product.events" :key="event">{{ event }}</span>
                </div>
                <div class="product-interest">
                    <div class="interest-high">
                        <p>최고</p> <span>{{ product.prime_interest_rate }}%</span>
                    </div>
                    <div>
                        <p>기본</p> <span>{{ product.interest_rate }}%</span>
                    </div>
                </div>
                <a :href="product.product_link" class="info-btn">공식홈에서 더 알아보기</a>
            </div>

            <div class="product-detail"> <!--상품 안내-->
                <h2>상품 안내</h2>
                <div class="product-detail-list">
                    <div class="product-detail-item">
                        <dt>금액</dt>
                        <dd>{{ product.join_amount_text }}</dd>
                    </div>
                    <div class="product-detail-item">
                        <dt>기간</dt>
                        <dd v-html="product.join_period_text"></dd>
                    </div>
                    <div class="product-detail-item">
                        <dt>가입방법</dt>
                        <dd v-html="product.join_way"></dd>
                    </div>
                    <div class="product-detail-item">
                        <dt>대상</dt>
                        <dd>{{ product.join_member }}</dd>
                    </div>
                    <div class="product-detail-item">
                        <dt>우대조건</dt>
                        <dd v-html="product.prime_conditions"></dd>
                    </div>
                    <div class="product-detail-item">
                        <dt>이자지급</dt>
                        <dd v-html="product.interest_payment"></dd>
                    </div>
                    <div class="product-detail-item">
                        <dt>유의사항</dt>
                        <dd v-html="product.note"></dd>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onBeforeMount, onMounted, ref, computed } from 'vue';
import { onBeforeRouteUpdate, useRoute } from 'vue-router';
import { useRecommendStore } from '@/stores/recommend';

const route = useRoute();
const recommendStore = useRecommendStore();
const product = computed(() => recommendStore.product)


onMounted(async () => {
    const category = route.params.category;
    const productId = Number(route.params.productId);
    await recommendStore.getProductDetail(category, productId);
});

onBeforeRouteUpdate(async (to) => {
    const category = to.params.category;
    const productId = Number(to.params.productId);
    await recommendStore.getProductDetail(category, productId);
});
</script>

<style scoped>
.container {
    background-color: #FAE7DB;
    width: 100%;
    height: 100vh;
    display: flex;
    margin: 0px;
    padding: 0px;
    flex-direction: column;
}

.product-title {
    color: #8d8d8d;
    margin-bottom: 10px;
    padding-bottom: 10px;
    border-bottom: 1px solid #dfdcdc;
}

.product-container {
    margin-top: 40px;
}

.bank-name {
    margin-top: 5px;
    color: #a7a7a7;
}

.product-event {
    margin-top: 5px;
}

.product-event>span {
    background-color: #E9E9E9;
    border-radius: 15px;
    padding: 0.5px 10px;
    font-size: 12px;
    color: #FF6708;
}

.product-info {
    width: 800px;
    display: flex;
    flex-direction: column;
    margin-right: auto;
    margin-left: auto;
    background-color: white;
    padding: 30px;
    border-radius: 30px;
}

.product-interest {
    margin-top: 20px;
    display: flex;
    gap: 20px;

}

.product-interest p {
    color: #BCBCBC;
    font-size: 14px;
    margin-bottom: 10px;
}

.product-interest span {
    color: #FF6708;
    font-weight: 700;
    font-size: 18px;
}

.interest-high {
    height: 55px;
    border-right: 0.5px solid #f1f1f1;
    padding-right: 20px;
}

.product-detail {
    width: 800px;
    height: auto;
    flex-direction: column;
    margin-right: auto;
    margin-left: auto;
    margin-top: 10px;
    background-color: white;
    padding: 30px;
    border-radius: 30px;
}

.product-detail-list {
    display: table;
    
}

.product-detail-item {
    display: table-row;
    unicode-bidi: isolate;
    padding: 10px 0;
}

.product-detail-item dt,
.product-detail-item dd {
    display: table-cell;
    unicode-bidi: isolate;
    padding: 5px 0;

}

.product-detail-item dt {
    padding-right: 10px;
    white-space: nowrap;
    white-space-collapse: collapse;
    text-wrap-mode: nowrap;
    font-weight: 700;
    color: #FF6708;
}

.product-detail-item dd {
    margin-inline-start: 40px;
}

.info-btn {
    margin-top: 30px;
    padding: 5px 30px;
    margin-right: auto;
    margin-left: auto;
    display: flex;
    justify-content: center;
    font-size: 20px;
    border: none;
    color: white;
    background-color: #FF6708;
    border-radius: 20px;
    cursor: pointer;
}

.product-detail>h2 {
    color: #8d8d8d;
    border-bottom: 1px solid #dfdcdc;
    padding-bottom: 10px;
    margin-bottom: 20px;
}

.product-detail>p {
    margin: 9px 2px;
    color: #8d8d8d;
}
</style>