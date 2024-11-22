<template>
    <div class="signup-container" v-if="store.user">
        <h2 class="signup-title">내 정보 수정</h2>
        <form class="signup-form" @submit.prevent="handleSubmit">
            <!-- 기본 정보 -->
            <div class="input-group">
                <p>이름: {{ store.user.name }}</p>
                <p>생년월일: {{ store.user.birth_date }}</p>
                <p>아이디: {{ store.user.email }}</p>
            </div>

            <!-- 비밀번호 변경 버튼 -->
            <div class="password-change-section">
                <button type="button" class="goal-btn" :class="{ 'active': showPasswordFields }"
                    @click="togglePasswordChange">
                    {{ showPasswordFields ? '닫기' : '비밀번호 변경' }}
                </button>
            </div>

            <!-- 비밀번호 변경 필드 -->
            <div v-show="showPasswordFields">
                <p>비밀번호</p>
                <div class="input-group">
                    <input type="password" class="input-field" placeholder="새로운 비밀번호를 입력하세요"
                        v-model="formData.password1">
                    <p class="password-require">* 비밀번호는 대소 문자, 특수문자를 포함한 8자리 이상으로 설정해주세요</p>
                </div>

                <p>비밀번호 확인</p>
                <div class="input-group">
                    <input type="password" class="input-field" placeholder="새로운 비밀번호를 한번 더 입력해주세요"
                        v-model="formData.password2">
                </div>
            </div>

            <p>자산</p>
            <div class="input-group">
                <div class="man">
                    <input type="text" class="input-field" placeholder="자산을 입력하세요" v-model="formData.asset"
                        style="text-align: end; padding-right: 50px; padding-top: 10px;">
                    <span class="man-won">만원</span>
                    <!-- <p class="asset-min">* 만 단위 이상 기입</p> -->
                </div>
            </div>

            <p>저축 목표</p>
            <div class="goal-group">
                <button 
                    v-for="goal in goals" 
                    :key="goal" 
                    type="button" 
                    class="goal-btn"
                    :class="{'active': formData.saving_purpose.includes(goal) }" 
                    @click="toggleGoal(goal)">
                    {{ goalsToKor[goal] }}
                </button>
            </div>

            <p>저축 기간 (개월)</p>
            <div class="savings-slider-wrapper">
                <div class="savings-amount-slider">
                    <input type="radio" name="savings-period" id="amount1" value="0" v-model="formData.saving_period" disabled>
                    <label for="amount1" data-amount="0"></label>
                    <input type="radio" name="savings-period" id="amount2" value="6" v-model="formData.saving_period">
                    <label for="amount2" data-amount="6"></label>
                    <input type="radio" name="savings-period" id="amount3" value="12" v-model="formData.saving_period">
                    <label for="amount3" data-amount="12"></label>
                    <input type="radio" name="savings-period" id="amount4" value="24" v-model="formData.saving_period">
                    <label for="amount4" data-amount="24"></label>
                    <input type="radio" name="savings-period" id="amount5" value="36" v-model="formData.saving_period">
                    <label for="amount5" data-amount="36"></label>
                </div>
            </div>

            <div class="input-group">
                <div class="man">
                    <p class="deb-amount">저축 금액</p>
                    <input type="text" class="input-field" v-model="formData.saving_amount" placeholder="금액을 입력하세요"
                        style="text-align: end; padding-right: 50px; padding-top: 10px;">
                    <span class="man-won2">만원</span>
                    <!-- <p class="asset-min">* 만 단위 이상 기입</p> -->
                </div>
            </div>
            <button type="submit" class="submit-btn">완료</button>
        </form>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/user';
import router from '@/router';

const store = useUserStore();
const selectedGoals = ref([]);
const showPasswordFields = ref(false);

const formData = ref({
    password1: '',
    password2: '',
    asset: '',
    saving_purpose: [],
    saving_amount: '',
    saving_period: ''
});

const togglePasswordChange = () => {
    showPasswordFields.value = !showPasswordFields.value;
    if (!showPasswordFields.value) {
        formData.value.password1 = '';
        formData.value.password2 = '';
    }
};

const toggleGoal = (goal) => {
    const index = selectedGoals.value.indexOf(goal);
    if (index > -1) {
        selectedGoals.value.splice(index, 1);
    } else {
        if (selectedGoals.value.length >= 3) {
            console.log(selectedGoals.value)
            alert('목표 설정은 최대 3개까지만 가능합니다.');
            return;
        }
        selectedGoals.value.push(goal);
    }
    formData.value.saving_purpose = [...selectedGoals.value];
};

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


const handleSubmit = () => {
    const updateData = {};

    // 비밀번호 필드가 보이고 있고, 비밀번호가 입력된 경우에만 검증


    
    if (showPasswordFields.value && (formData.value.password1 || formData.value.password2)) {
        // 1. 유효성 검사 : 비밀번호와 비밀번호 확인이 다른 경우
        if (formData.value.password1 != formData.value.password2) {
            alert('비밀번호가 다릅니다.')
        }
        // 2. 유효성 검사 : 비밀번호 자리수 확인
        if (formData.value.password1.length < 8 || formData.value.password2.length < 8) {
            alert('비밀번호는 8자리 이상으로 설정해주세요.');
            return; // 함수 실행 중단
        }

        
        updateData.password1 = formData.value.password1;
        updateData.password2 = formData.value.password2;
    }

    // 나머지 데이터 업데이트
    if (formData.value.asset) updateData.asset = formData.value.asset;
    if (selectedGoals.value.length > 0) updateData.saving_purpose = selectedGoals.value;
    if (formData.value.saving_amount) updateData.saving_amount = formData.value.saving_amount;
    if (formData.value.saving_period) updateData.saving_period = formData.value.saving_period;

    // 유효성 검사를 통과한 경우에만 API 호출
    store.updateUserInfo(updateData)
        .then(() => {
            console.log('정보 업데이트 성공');
        })
        .catch(error => {
            console.error('정보 업데이트 실패:', error);
        });
};

onMounted(() => {
    store.getUserInfo()
        .then(() => {
            if (store.user) {
                formData.value.asset = store.user.asset || '';
                formData.value.saving_amount = store.user.saving_amount || '';
                formData.value.saving_period = store.user.saving_period || '';
                // 저축 목표 초기화 로직 수정
                if (store.user.saving_purpose) {
                    // 배열이 아닌 경우 배열로 변환
                    const purposeArray = Array.isArray(store.user.saving_purpose) 
                        ? store.user.saving_purpose 
                        : [store.user.saving_purpose];
                    
                    // 최대 3개까지만 설정
                    selectedGoals.value = purposeArray.slice(0, 3);
                    formData.value.saving_purpose = [...selectedGoals.value];
                    console.log(selectedGoals.value)
                    console.log(formData.value.saving_purpose)
                }
            }
        })
        .catch(error => {
            console.error('사용자 정보 로드 실패:', error);
        });
});
</script>

<style scoped>
/* 컨테이너 스타일 */
.signup-container {
    width: 100%;
    max-width: 500px;
    margin: 20px auto;
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

.input-group>p {
    margin: 20px 0;
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

.password-change-section {
    margin-bottom: 20px;
}

.asset-min {
    font-size: 12px;
    color: #fc8a44;
    padding-left: 10px;
    font-weight: 350;
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