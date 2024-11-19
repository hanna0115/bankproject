<template>
    <div class="exchange-rate">
        <h2>환율 계산기</h2>
        <div class="exchange-rate-box">
            <form>
                <div class="input-box">
                    <label for="cur-nm">통화 선택</label>
                    <select name="cur-nm" id="cur-nm">
                        <option value="" selected>국가를 선택하세요</option>
                        <option value="">국가명 통화명</option>
                    </select>
                </div>
                <div class="input-box">
                    <label for="">금액</label>
                    <input type="text" placeholder="계산할 금액을 입력하세요">
                </div>
                <button>계산하기</button>
            </form>

            <div class="exchange-krw">
                <p>KRW</p>
            </div>
        </div>

        <div class="graph">
            환율 그래프 넣기
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>
.exchange-rate {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.exchange-rate h2 {
    margin: 100px auto 30px;
    color: #ff6708;
}

.exchange-rate-box {
    width: 80%;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1);
}

.exchange-rate-box form {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.input-box {
    position: relative;
}

.input-box label {
    position: absolute;
    top: -11px;
    left: 11px;
    font-size: 14px;
    background-color: #fff;
}

.input-box select,
.input-box input {
    padding: 8px 10px;
    border: 1px solid #BCBCBC;
    border-radius: 5px;
}

.exchange-rate-box button {
    padding: 8px 10px;
    border-radius: 5px;
    color: #fff;
    background-color: #FFB07E;
}

.graph {
    margin: 20px 0;
}
</style>