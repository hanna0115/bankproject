import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import router from "@/router";

export const useUserStore = defineStore("user", () => {
  const url = 'http://127.0.0.1:8000'
//   const isAuthenticated = ref(false)
  const token = ref(null)
  const isLoggedIn = computed(() => !!token.value)
  const user = ref(null)
  const userPK = ref(null)

  // 1. 회원가입
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
      const password = password1
      logIn({ email, password })
      router.push('/')  // 회원가입 성공 시 홈으로 이동
    })
    .catch((error) => {
        console.error('회원가입 실패:', error)
    })
  }

  // 2. 로그인
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
        fetchUserInfo()
    })
    .catch((error) => {
        if (error.response?.status === 400) {
            throw new Error ('이메일 또는 비밀번호가 올바르지 않습니다.')
        } else {
            throw new Error ('로그인 중 오류가 발생했습니다.')
        }
    })
  }

  // 2-1. 사용자 정보 가져오기
  const fetchUserInfo = async () => {
    try {
      const response = await axios.get(`${url}/accounts/user/`, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      userPK.value = response.data.pk
    } catch (error) {
      console.error('사용자 정보를 가져오는 데 실패했습니다:', error)
      throw new Error('사용자 정보를 가져오는 데 실패했습니다.')
    }
  }

  // 3. 로그아웃
  const logOut = () => {
    token.value = null
    router.push('/login')
  }

  // 4. 마이페이지
  const getUserInfo = function () {
    return new Promise((resolve, reject) => {
        axios({
            method: 'get',
            url: `${url}/accounts/profile/${userPK.value}/`,
            headers: {
                Authorization: `Token ${token.value}`
            }
        })
        .then(res => {
            user.value = res.data;
            resolve(res.data);
        })
        .catch(err => {
            console.log('유저 정보 가져오기 실패', err);
            reject(err);
        });
    });
};


const updateUserInfo = (payload) => {
  return new Promise((resolve, reject) => {
      axios({
          method: 'put',
          url: `${url}/accounts/profile/update/`,
          data: payload,
          headers: {
              Authorization: `Token ${token.value}`
          }
      })
      .then(response => {
          user.value = response.data;
          router.push(`/profile/${userPK.value}`);
          resolve(response.data);
      })
      .catch(error => {
          console.log('사용자 정보 업데이트 실패:', error);
          reject(error);
      });
  });
};
  
  return { url, signUp, logIn, token, logOut, isLoggedIn, user, userPK, getUserInfo, updateUserInfo }
}, { persist: true });
