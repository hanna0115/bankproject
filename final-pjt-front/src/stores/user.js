import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import router from "@/router";

export const useUserStore = defineStore("user", () => {
  const url = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLoggedIn = computed(() => !!token.value)
  const user = ref(null)
  const userPK = ref(null)

  // 1. 회원가입
  const signUp = async function (payload) {
    const { name, email, birth_date, asset, saving_purpose, saving_amount, saving_period, password1, password2 } = payload;

    try {
        const response = await axios({
            method: 'post',
            url: `${url}/accounts/signup/`,
            data: {
              name, email, birth_date, asset, saving_purpose, saving_amount, saving_period, password1, password2
            }
        });

        console.log('회원가입이 완료되었습니다.');
        
        // 로그인 요청
        const password = password1;
        await logIn({ email, password });
        
        router.push({ name: 'home' });
    } catch (error) {
        console.error('회원가입 실패:', error);
        throw error;
    }
  };

  // 2. 로그인
  const logIn = async (payload) => {
    const { email, password } = payload;
    try {
        const response = await axios({
            method: 'post',
            url: `${url}/accounts/login/`,
            data: { email, password }
        });

        token.value = response.data.key;
        localStorage.setItem('token', response.data.key);

        // 사용자 정보를 가져옵니다.
        await fetchUserInfo();
        await getUserInfo();

        router.push('/');
    } catch (error) {
        console.error('로그인 실패:', error);
        if (error.response?.status === 400) {
            throw new Error('이메일 또는 비밀번호가 올바르지 않습니다.');
        }
        throw new Error('로그인 중 오류가 발생했습니다.');
    }
  }

  // 2-1. 사용자 정보 가져오기
  const fetchUserInfo = async () => {
    try {
      const response = await axios.get(`${url}/accounts/user/`, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      });
      userPK.value = response.data.pk;
    } catch (error) {
      console.error('사용자 정보를 가져오는 데 실패했습니다:', error);
      throw error;
    }
  }

  // 3. 로그아웃
  const logOut = async () => {
    try {
      await axios({
        method: 'post',
        url: `${url}/accounts/logout/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      });
      token.value = null;
      user.value = null;
      userPK.value = null;
      localStorage.removeItem('token');
      router.push('/login');
    } catch (error) {
      console.error('로그아웃 실패:', error);
      throw error;
    }
  }

  // 4. 마이페이지
  const getUserInfo = async function () {
    try {
      const response = await axios({
        method: 'get',
        url: `${url}/accounts/profile/${userPK.value}/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      });
      user.value = response.data;
      return response.data;
    } catch (error) {
      console.error('유저 정보 가져오기 실패:', error);
      throw error;
    }
  };

  const updateUserInfo = async (payload) => {
    try {
      const response = await axios({
        method: 'put',
        url: `${url}/accounts/profile/update/`,
        data: payload,
        headers: {
          Authorization: `Token ${token.value}`
        }
      });
      user.value = response.data;
      router.push(`/profile/${userPK.value}`);
      return response.data;
    } catch (error) {
      console.error('사용자 정보 업데이트 실패:', error);
      throw error;
    }
  };

  const getAllUserInfo = () => {
    axios({
      method:'get',
      url:`${url}/accounts/user/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((response) => {
      console.log(response.data)
    })
    .catch((error) => {
      console.log('가져오기 실패!:', error)
    })
  }


  return { 
    url, 
    signUp, 
    logIn, 
    token, 
    logOut, 
    isLoggedIn, 
    user, 
    userPK, 
    getUserInfo, 
    updateUserInfo,
    getAllUserInfo,

  }
}, { persist: true });