import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import router from "@/router";

export const useUserStore = defineStore("user", () => {
  const url = 'http://127.0.0.1:8000'
//   const isAuthenticated = ref(false)
  const token = ref(null)

  const signUp = function (payload) {
    const {name, email, birth_date, asset, saving_purpose, saving_amount, saving_period, password1, password2} = payload

    axios({
        method:'post',
        url: `${url}/accounts/signup/`,
        data: {
            name, email, birth_date, asset, saving_purpose, saving_amount, saving_period, password1, password2
        }
    })
    .then((response) => {
    //   token.value = response.data.token
    //   localStorage.setItem('token', response.data.token)
    //   isAuthenticated.value = true
      console.log('회원가입이 완료되었습니다.')
      router.push('/')  // 회원가입 성공 시 홈으로 이동
    })
    .catch((error) => {
        console.error('회원가입 실패:', error)
    })
  }

  const logIn = (payload) => {
    const email = payload.email
    const password = payload.password
    axios({
        method: 'post',
        url: `${url}/accounts/login/`,
        data: {
            email, password
        }
    })
    .then(response => {
        console.log('로그인이 완료되었습니다.')
        console.log(response.data)
        router.push('/')
        token.value = response.data.key
    })
    .catch((error) => {
        if (error.response?.status === 400) {
            throw new Error ('이메일 또는 비밀번호가 올바르지 않습니다.')
        } else {
            throw new Error ('로그인 중 오류가 발생했습니다.')
        }
    })
  }
  
  return { url, signUp, logIn, token};
});
