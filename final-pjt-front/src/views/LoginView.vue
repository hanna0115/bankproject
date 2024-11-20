<template>
    <div class="login">
        <h2 class="title">Welcome to</h2>

        <form class="login-form" @submit.prevent="logIn">
            <div>
                <label for="id">아이디</label>
                <input type="text" id="id" placeholder="example@email.com" v-model.trim="email" required>
            </div>
            <div>
                <label for="password">비밀번호</label>
                <input type="password" id="password" placeholder="********" v-model.trim="password" required>
            </div>
            <input type="submit" value="로그인">
        </form>

        <div class="user-nav">
            <button class="signup-btn" 
            @click="router.push('/signup')">회원가입</button>
            <span> | </span>
            <p>아이디 찾기</p>
            <span> | </span>
            <p>비밀번호 찾기</p>
        </div>
    </div>
</template>

<script setup>

import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';

const router = useRouter()
const store = useUserStore()

const email = ref(null)
const password = ref(null)

const logIn = () => {
    const payload = {
        email: email.value,
        password: password.value
    }
    store.logIn(payload)
}


</script>

<style scoped>
.login {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin-top: 150px;
}

.login .title {
  color: #FF6709;
  font-weight: bold;
  font-size: 30px;
}

.login-form {
    width: 350px;
    margin-top: 60px;
}

.login-form div {
    display: flex;
    justify-content: center;
    flex-direction: column;
    margin: 15px 0;
}

.login-form label {
    margin-bottom: 5px;
    font-weight: 700;
    color: #FFB07E;
}

.login-form input {
    width: 100%;
    padding: 10px 0;
    border: none;
    border-bottom: 1.35px solid #909090;
    
}

.login-form input:focus {
    outline: none;
}

.login-form input[type='submit'] {
  background-color: rgba(255,103,8,0.6);
  color: white;
  margin-top: 30px;
  padding: 10px 12px; 
  font-weight: 700;
  font-size: 16px;
  border: none;
  border-radius: 30px;
  cursor: pointer;
}

.user-nav {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 15px;
    font-size: 14px;
    color: #898989;
}

.user-nav p {
    margin: 0px;
    padding: 5px;
}

.signup-btn {
    margin: 0px;
    padding: 5px;
    border: 0;
    background-color: transparent;
    color: #898989;
    cursor: pointer;
}
</style>