import { defineStore } from 'pinia';
import { ref, computed, watch } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { useUserStore } from './user';

export const useCommunityStore = defineStore("community", () => {
  const API_URL = 'http://127.0.0.1:8000';
  const userStore = useUserStore()
  const posts = ref([])

  const selectedCategory = ref('all')
  const filteredPosts = ref([])
  const currentPage = ref(1)
  const router = useRouter()

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


  // 게시글 생성
  const createPost = function (title, content, selectedTag) {
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
            router.push({ name: 'community'})
        })
        .catch(err => console.log('게시글 생성 오류', err))
  }

  const post = ref(null)

  const getPostDetail = function (postId) {
    axios({
        method: 'get',
        url: `${API_URL}/posts/detail/${postId}/`
    })
    .then(res => {
        post.value = res.data; // 이 부분은 store.post로 변경할 수 있습니다.
    })
    .catch(err => console.log('단일 게시글 조회 실패', err));
  };

  
watch(post.num_seen, (newVal, oldVal) => {
    post.value.num_seen = res.data.num_seen
})

  return { 
    API_URL,
    posts,
    post,
    getPosts, 
    selectedCategory, 
    updateCategory, 
    getFilteredPosts,
    getCurrentCategory,
    currentPage,
    createPost,
    getPostDetail
  }
})