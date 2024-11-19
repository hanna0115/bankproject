<template>
    <div class="signup-container">
        <h2 class="signup-title">회원가입</h2>
        <form class="signup-form">
            <div class="input-group">
                <p>이름</p>
                <input type="text" class="input-field" placeholder="이름을 입력하세요">
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
                <input type="text" class="input-field" placeholder="이메일 주소">
                <span>@</span>
                <select class="select-box">
                    <option value="naver.com">naver.com</option>
                    <option value="google.com">google.com</option>
                    <option value="hanmail.net">hanmail.net</option>
                    <option value="nate.com">nate.com</option>
                    <option value="kakao.com">kakao.com</option>
                </select>
            </div>

            <p>비밀번호</p>
            <div class="input-group">
                <input type="password" class="input-field" placeholder="비밀번호를 입력하세요">
            </div>

            <p>자산</p>
            <div class="input-group">
                <input type="password" class="input-field" placeholder="자산을 입력하세요">
            </div>

            <p>저축 목표</p>
            <div class="goal-group">
                <button v-for="goal in goals" :key="goal" type="button" class="goal-btn"
                    :class="{ 'active': selectedGoals.includes(goal) }" @click="toggleGoal(goal)">
                    {{ goal }}
                </button>
            </div>

            <p>저축 기간 (개월)</p>
            <div class="savings-slider-wrapper">
                <div class="savings-amount-slider">
                    <input type="radio" name="savings-amount" id="amount1" value="1" required>
                    <label for="amount1" data-amount="0"></label>
                    <input type="radio" name="savings-amount" id="amount2" value="2" required>
                    <label for="amount2" data-amount="6"></label>
                    <input type="radio" name="savings-amount" id="amount3" value="3" required>
                    <label for="amount3" data-amount="12"></label>
                    <input type="radio" name="savings-amount" id="amount4" value="4" required>
                    <label for="amount4" data-amount="24"></label>
                    <input type="radio" name="savings-amount" id="amount5" value="5" required>
                    <label for="amount5" data-amount="36"></label>
                </div>
            </div>

            <div class="input-group">
                <p class="deb-amount">저축 금액 (만원)</p>
                <input type="text" class="input-field" placeholder="금액을 입력하세요">
            </div>
            <button type="submit" class="submit-btn"
            @click="router.push('/')">완료</button>
        </form>
    </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useRouter } from 'vue-router';

const goals = [
    '내집마련',
    '교육비',
    '의료비',
    '결혼자금',
    '노후자금',
    '시드머니',
    '여행자금',
    '위시리스트'
]

const router = useRouter()


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
const selectedGoals = ref([])

// 목표 토글 함수
const toggleGoal = (goal) => {
    if (selectedGoals.value.includes(goal)) {
        // 이미 선택된 목표라면 제거
        selectedGoals.value = selectedGoals.value.filter(g => g !== goal)
    } else {
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