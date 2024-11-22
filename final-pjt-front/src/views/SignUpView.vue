<template>
    <div class="signup-container">
        <h2 class="signup-title">회원가입</h2>
        <form class="signup-form" @submit.prevent="signUp">
            <div class="input-group">
                <p>이름</p>
                <input type="text" class="input-field" placeholder="이름을 입력하세요" v-model.trim="username">
            </div>

            <p>생년월일</p>
            <div class="birth-select-group">
                <select class="select-box" v-model="selectedYear">
                    <option disabled value="">년도</option>
                    <option v-for="year in years" :key="year" :value="year">
                        {{ year }}
                    </option>
                </select>
                <select class="select-box" v-model="selectedMonth">
                    <option disabled value="">월</option>
                    <option v-for="month in months" :key="month" :value="month">
                        {{ month }}
                    </option>
                </select>
                <select class="select-box" v-model="selectedDay">
                    <option disabled value="">일</option>
                    <option v-for="day in availableDays" :key="day" :value="day">
                        {{ day }}
                    </option>
                </select>
            </div>

            <p>아이디</p>
            <div class="email-input-group">
                <input type="text" class="input-field" placeholder="이메일 주소" v-model.trim="email">
                <span>@</span>
                <select class="select-box" v-model="emailDomain">
                    <option value="naver.com">naver.com</option>
                    <option value="google.com">google.com</option>
                    <option value="hanmail.net">hanmail.net</option>
                    <option value="nate.com">nate.com</option>
                    <option value="kakao.com">kakao.com</option>
                </select>
            </div>

            <p>비밀번호</p>
            <div class="input-group">
                <input type="password" class="input-field" placeholder="비밀번호를 입력하세요" v-model.trim="password1">
                <p class="password-require">* 비밀번호는 대소 문자, 특수문자를 포함한 8자리 이상으로 설정해주세요</p>
            </div>

            <p>비밀번호 확인</p>
            <div class="input-group">
                <input type="password" class="input-field" placeholder="비밀번호를 다시 한번 더 입력해주세요" v-model.trim="password2">
            </div>

            <p>자산</p>
            <div class="input-group">
                <div class="man">
                    <input type="text" class="input-field" placeholder="자산을 입력하세요" v-model.number="asset"
                        style="text-align: end; padding-right: 50px; padding-top: 10px;">
                    <span class="man-won">만원</span>
                    <!-- <p class="asset-min">* 만 단위</p> -->
                </div>
            </div>

            <p>저축 목표</p>
            <div class="goal-group">
                <button v-for="goal in goals" :key="goal" type="button" class="goal-btn"
                    :class="{ 'active': selectedGoals.includes(goal) }" @click="toggleGoal(goal)">
                    {{ goalsToKor[goal] }}
                </button>
            </div>

            <p>저축 기간 (개월)</p>
            <div class="savings-slider-wrapper">
                <div class="savings-amount-slider">
                    <input type="radio" name="savings-amount" id="amount1" value="0" v-model="savingPeriod" disabled>
                    <label for="amount1" data-amount="0"></label>
                    <input type="radio" name="savings-amount" id="amount2" value="6" v-model="savingPeriod">
                    <label for="amount2" data-amount="6"></label>
                    <input type="radio" name="savings-amount" id="amount3" value="12" v-model="savingPeriod">
                    <label for="amount3" data-amount="12"></label>
                    <input type="radio" name="savings-amount" id="amount4" value="24" v-model="savingPeriod">
                    <label for="amount4" data-amount="24"></label>
                    <input type="radio" name="savings-amount" id="amount5" value="36" v-model="savingPeriod">
                    <label for="amount5" data-amount="36"></label>
                </div>
            </div>

            <div class="input-group">
                <div class="man">
                    <p class="deb-amount">저축 금액</p>
                    <div class="input-end-start">
                        <input type="text" class="input-field" placeholder="금액을 입력하세요" v-model.number="savingAmount"
                            style="text-align: end; padding-right: 50px; padding-top: 10px;">
                    </div>
                    <span class="man-won2">만원</span>
                    <!-- <p class="asset-min">* 만 단위 이상 기입</p> -->
                </div>
            </div>
            <button type="submit" class="submit-btn">완료</button>
        </form>
    </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';

const router = useRouter()
const store = useUserStore()

const signUp = function () {
    if (password1.value !== password2.value) {
        alert('비밀번호가 달라요!')
        return
    }

    const payload = {
        name: username.value,
        email: fullEmail.value,
        birth_date: `${selectedYear.value}-${String(selectedMonth.value).padStart(2, '0')}-${String(selectedDay.value).padStart(2, '0')}`,
        asset: parseInt(asset.value),
        saving_purpose: selectedGoals.value,
        saving_amount: parseInt(savingAmount.value),
        saving_period: parseInt(savingPeriod.value),
        password1: password1.value,
        password2: password2.value,
    }

    store.signUp(payload)
        .catch(error => {
            if (error.response?.data?.email) {
                alert('이미 가입된 이메일이 존재합니다.')
            } else {
                alert('이미 가입된 이메일이 존재합니다.')
            }
        })
}


//폼 데이터
const username = ref('')
const email = ref('')
const emailDomain = ref('naver.com')
const password1 = ref('')
const password2 = ref('')
const asset = ref('')
const savingAmount = ref('')
const savingPeriod = ref('')
const selectedGoals = ref([])

// 이메일 계산

const fullEmail = computed(() => {
    if (email.value && emailDomain.value) {
        return `${email.value}@${emailDomain.value}`
    }
})

const goals = [
    'home',
    'education',
    'medication',
    'wedding',
    'future',
    'seedmoney',
    'travel',
    'wishlist'
]

const goalsToKor = {
        'home': '내집마련',
        'education': '교육비',
        'medication': '의료비',
        'wedding': '결혼자금',
        'future': '노후자금',
        'seedmoney': '시드머니',
        'travel': '여행자금',
        'wishlist': '위시리스트'
    }

// 생년월일 관련 코드
const currentYear = new Date().getFullYear()
const years = Array.from({ length: currentYear - 1899 }, (_, i) => currentYear - i)
const months = Array.from({ length: 12 }, (_, i) => i + 1)

const selectedYear = ref('')
const selectedMonth = ref('')
const selectedDay = ref('')

// 월별 일수 계산
const getDaysInMonth = (year, month) => {
    if (!year || !month) return []

    const daysIn31 = [1, 3, 5, 7, 8, 10, 12]
    const daysIn30 = [4, 6, 9, 11]

    if (daysIn31.includes(month)) {
        return Array.from({ length: 31 }, (_, i) => i + 1)
    } else if (daysIn30.includes(month)) {
        return Array.from({ length: 30 }, (_, i) => i + 1)
    } else {
        const isLeapYear = (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)
        return Array.from({ length: isLeapYear ? 29 : 28 }, (_, i) => i + 1)
    }
}

// 사용 가능한 일자 계산
const availableDays = computed(() => {
    return getDaysInMonth(selectedYear.value, selectedMonth.value)
})

// 월이 변경될 때 일자 재설정
watch([selectedYear, selectedMonth], () => {
    const days = getDaysInMonth(selectedYear.value, selectedMonth.value)
    if (selectedDay.value > days.length) {
        selectedDay.value = ''
    }
})

// 선택된 목표들을 배열로 관리

// 목표 토글 함수
const toggleGoal = (goal) => {

    console.log(goal)
    if (selectedGoals.value.includes(goal)) {
        // 이미 선택된 목표라면 제거
        selectedGoals.value = selectedGoals.value.filter(g => g !== goal)
    } else if (selectedGoals.value.length > 2) {
        alert('목표 설정은 최대 3개까지만 가능합니다.')
    } 

    else {
        // 선택되지 않은 목표라면 추가
        selectedGoals.value.push(goal)
    }
}



</script>

<style scoped>
/* 컨테이너 스타일 */
.signup-container {
    width: 100%;
    max-width: 500px;
    margin: 60px auto;
    padding: 20px;
}

.signup-title {
    color: #FF6708;
    text-align: center;
    font-size: 24px;
    margin-bottom: 40px;
}

/* 입력 필드 공통 스타일 */
p {
    color: #808080;
    margin-bottom: 8px;
    margin-left: 3px;
    font-size: 14px;
}

.input-group {
    margin-bottom: 30px;
}



.man {
    position: relative;
}

.man-won {
    position: absolute;
    width: 30px;
    right: 10px;
    top: 10px;
    color: #808080;
}

.man-won2 {
    position: absolute;
    width: 30px;
    right: 10px;
    top: 40px;
    color: #808080;
}

.password-require {
    font-size: 12px;
    color: #fc8a44;
    padding-left: 10px;
    font-weight: 350;
}

.asset-min {
    font-size: 12px;
    color: #fc8a44;
    padding-left: 10px;
    font-weight: 350;
    justify-content: end;
}

.input-field {
    width: 100%;
    padding: 12px;
    border: 1px solid #E5E5E5;
    border-radius: 8px;
    font-size: 14px;
}

.input-field::placeholder {
    color: #999;
}

/* 생년월일 선택 스타일 */
.birth-select-group {
    display: flex;
    gap: 10px;
    margin-bottom: 30px;
}

.select-box {
    flex: 1;
    padding: 12px;
    border: 1px solid #E5E5E5;
    border-radius: 8px;
    background: white;
    font-size: 14px;
}

/* 이메일 입력 스타일 */
.email-input-group {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 30px;
}

.email-input-group .input-field {
    flex: 1;
}

.email-input-group span {
    color: #666;
}



/* 목표 버튼 스타일 */
.goal-group {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 30px;
    justify-content: center;
    padding: 0 10px;
}

.goal-btn {
    width: 100px;
    padding: 8px 0;
    border: 1px solid #E5E5E5;
    border-radius: 20px;
    background: white;
    cursor: pointer;
    font-size: 13px;
    transition: all 0.3s ease;
    text-align: center;
}

.goal-btn:hover {
    border-color: #FFB07E;
    color: #FFB07E;
}

.goal-btn.active {
    background: #FFB07E;
    color: white;
    border-color: #FFB07E;
}

/* 슬라이더 스타일 */
.savings-slider-wrapper {
    margin: 40px 0;
}

.savings-amount-slider {
    display: flex;
    flex-direction: row;
    align-content: stretch;
    position: relative;
    width: 100%;
    height: 40px;
    user-select: none;
}

.savings-amount-slider::before {
    content: " ";
    position: absolute;
    height: 2px;
    width: 80%;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: #E5E5E5;
}

.savings-amount-slider input {
    display: none;
}

.savings-amount-slider label {
    display: inline-block;
    position: relative;
    width: 20%;
    height: 100%;
    cursor: pointer;
}

.savings-amount-slider label::before {
    content: attr(data-amount);
    position: absolute;
    left: 50%;
    padding-top: 10px;
    transform: translate(-50%, 45px);
    font-size: 14px;
    opacity: 0.85;
    transition: all 0.15s ease-in-out;
}

.savings-amount-slider label::after {
    content: " ";
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 15px;
    height: 15px;
    border: 2px solid #E5E5E5;
    background: white;
    border-radius: 50%;
    transition: all 0.15s ease-in-out;
}

.savings-amount-slider label:hover::after {
    border-color: #FF6708;
    background: #FF6708;
    transform: translate(-50%, -50%) scale(1.25);
}

.savings-amount-slider input:checked+label::after {
    border-color: #FF6708;
    background: #FF6708;
    transform: translate(-50%, -50%) scale(0.75);
}

/* 제출 버튼 스타일 */
.submit-btn {
    width: 100%;
    padding: 15px;
    background: #FF6708;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    margin-top: 10px;
}

.submit-btn:hover {
    background: #ff7d2e;
}

.deb-amount {
    margin-top: 90px;
    margin-bottom: 10px;
}
</style>