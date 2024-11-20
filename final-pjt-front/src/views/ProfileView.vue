<template>
    <div class="container">
        <h2 class="title">마이 페이지</h2>
        <div class="content">
            <div>
                <p class="user-name"><span class="user-realname">오한나</span class="nim">님</p>
                <button class="modify-btn">내 정보 수정</button>
            </div>
            <div class="product">
                <span>내가 가입한 예적금 상품</span>
                <button class="product-btn">연동 하기</button>
            </div>
        </div>
        <ProductIItem />

    </div>
</template>

<script setup>

import ProductIItem from '@/components/ProductIItem.vue';

</script>

<style scoped>
.container {
    display: flex;
    width: 30%;
    flex-direction: column;
    margin: 0 auto;
    margin-top: 100px;
}

/* .content {
    margin-left: 180px;
} */

.title {
    margin: 0 auto;
    margin-bottom: 20px;
    font-weight: 700;
    color: #FFA46B;
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
</style>