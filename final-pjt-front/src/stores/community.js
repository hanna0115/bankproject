import { defineStore } from 'pinia';
import { ref, computed, watch } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { useUserStore } from './user';

export const useCommunityStore = defineStore("community", () => {
  const API_URL = 'http://127.0.0.1:8000';
  const userStore = useUserStore()
  const router = useRouter()


  // 게시글 목록 조회
  const posts = ref([])
  const selectedCategory = ref('all')
  const filteredPosts = ref([])
  const currentPage = ref(1)


  // 1. 전체 게시글 목록 조회
  const getPosts = function () {
    axios({
      method: 'get',
      url: `${API_URL}/posts/`
    })
      .then(res => {
        posts.value = res.data;
        filteredPosts.value = res.data
      })
      .catch(err => console.log('게시글을 가져오는 중 오류 발생:', err))
  };

  
  // 카테고리가 바뀔 때 게시물 필터링
  const updateCategory = (category) => {
    selectedCategory.value = category
    currentPage.value = 1
    filteredPosts.value = selectedCategory.value === 'all'
    ? posts.value
    : posts.value.filter(post => post.category === selectedCategory.value)
  };

  // 필터링된 게시글을 반환하는 computed 속성
  const getFilteredPosts = computed(() => filteredPosts.value);
  
  // 현재 선택된 카테고리를 반환하는 computed 속성
  const getCurrentCategory = computed(() => selectedCategory.value);

  // 작성일 데이터 형식 변환
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return `${date.getFullYear()}.${String(date.getMonth() + 1).padStart(2, '0')}.${String(date.getDate()).padStart(2, '0')}`;
}


  // 2. 게시글 생성
  const createPost = function (title, content, selectedTag) {
    // 입력값 검증
    if (title?.trim() === '') {
      alert('제목을 입력해주세요.');
      return;
    }
    if (content?.trim() === '') {
      alert('내용을 입력해주세요.');
      return;
    }
    if (!selectedTag || selectedTag === 'all') {
      alert('카테고리를 선택해주세요.');
      return;
    }

    axios({
        method: 'post',
        url: `${API_URL}/posts/`,
        data: {
            title,
            content,
            category: selectedTag
          },
          headers: {
            Authorization: `Token ${userStore.token}`
          }
    })
        .then(res => {
            selectedCategory.value = 'all'
            currentPage.value = 1
            router.push({ name: 'community'})
          })
          .catch(err => console.log('게시글 생성 오류', err))
        }
        
  
        // 3. 단일 게시글 - 조회
        const post = ref(null)
        
        const getPostDetail = function (postId) {
          return axios({
        method: 'get',
        url: `${API_URL}/posts/detail/${postId}/`
      })
      .then(res => {
        post.value = res.data
        return res.data
      })
    .catch(err => console.log('단일 게시글 조회 실패', err))
  };

  // 4. 단일 게시글 - 수정
  const updatePost = function (postId, title, content, selectedTag) {
    axios({
      method: 'put',
      url: `${API_URL}/posts/detail/${postId}/`,
      data: {
        title,
        content,
        category: selectedTag
      },
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
    .then(res => {
          selectedCategory.value = 'all'
          currentPage.value = 1
          console.log(res)
          router.push({ name: 'community'})
      })
      .catch(err => console.log('게시글 수정 오류', err))
}

  return { 
    API_URL,
    posts,
    selectedCategory,
    currentPage,
    getPosts,
    updateCategory,
    getFilteredPosts,
    getCurrentCategory,
    formatDate,
    createPost,
    post,
    getPostDetail,
    updatePost,
  }
})