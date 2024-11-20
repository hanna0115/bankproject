<template>
    <div class="main-content">
        <div class="product-content">
            <p>1 /</p>
            <img src="../assets/images/nh.png" alt="" class="bank-logo">
        </div>
        <div class="product">
            <div class="product-duration">
                <p class="bankname">농협은행</p>
                <span>NH고향사랑기부예금</span>
                <div class="duration-section">
                    <p>가입일: 2024.01.02</p>
                    <p>만기일: 2026.01.01 <span>(D-100)</span></p> 
                </div>
            </div>
            <div class="monthly-amount">
                <span>기본 이율: 2.0%</span>
                <p class="monthly">월 납입액: 100,000원</p>
                <p class="amount">1,000,000원</p>
            </div>
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>

.main-content {
    display: flex;
    /* margin: 0 auto; */
    border-bottom: 1px solid #BCBCBC;
    padding-bottom: 25px;
}

.product-content {
    display: flex;
}

.bank-logo {
    width: 20px;
    height: 25px;
    margin-left: 15px;
    margin-top: 5px;
}

.product {
    display: flex;
    justify-content: space-between;
    flex-grow: 2;
    
}

.product-duration {
    margin-left: 30px;
}

.product-duration > .bankname {
    color: #808080;
}

.product-duration > span {
    font-size: 18px;
    font-weight: 700;
}

.product-content {
    color: #FFA46B;
    font-size: 22px;
}

.duration-section > p {
    color: #BCBCBC;
    font-weight: 300;
}

.duration-section > p > span {
    color: #FFAE17;
}

.monthly-amount {
    align-self: end;
    text-align: end;
    margin-top: 73px;
}

.monthly-amount > span {
    color: #BCBCBC;
    font-weight: 300;
}

.monthly-amount > .monthly {
    color: #808080;
    font-weight: 700;
}

.monthly-amount > .amount {
    font-size: 20px;
    color: #FFA46B;
    font-weight: 700;

}

</style>