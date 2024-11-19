<template>
    <div class="container">
        <div class="product-container">

            <div class="product-info"> <!-- 상품 정보-->
                <h2 class="product-title">The 든든 예금</h2>
                <p class="bank-name">경남은행</p>
                <div class="product-event">
                    <span>특판</span> <span>특판</span> <span>특판</span>
                </div>
                <div class="product-interest">
                    <div class="interest-high">
                        <p>최고</p> <span>연 3.50%</span>
                    </div>
                    <div>
                        <p>기본</p> <span>연 2.35%</span>
                    </div>
                </div>
                <button
                class="info-btn">공식홈에서 더 알아보기</button>
            </div>
            
            <div class="product-detail"> <!--상품 안내-->
                <h2>상품 안내</h2>
                <p>기간:</p>
                <p>총액:</p>
                <p>가입방법:</p>
                <p>대상:</p>
                <p>우대조건:</p>
                <p>이자지급:</p>
                <p>유의:</p>
                <p>예금자보호:</p>
                
            </div>
        </div>
    </div>
</template>

<script setup>



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

.product-event > span {
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
    display: flex;
    flex-direction: column;
    margin-right: auto;
    margin-left: auto;
    margin-top: 10px ;
    background-color: white;
    padding: 30px;
    border-radius: 30px;
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

.product-detail > h2 {
    color: #8d8d8d;
    border-bottom: 1px solid #dfdcdc;
    padding-bottom: 10px;
    margin-bottom: 20px;
}

.product-detail > p {
    margin: 9px 2px;
    color: #8d8d8d;
}

</style>