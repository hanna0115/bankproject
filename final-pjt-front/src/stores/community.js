import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import axios from 'axios';

export const useCommunityStore = defineStore("community", () => {
  const API_URL = 'http://127.0.0.1:8000';
  let id = 0
  const posts = ref([])

  const selectedCategory = ref('all')
  const filteredPosts = ref([])
  const currentPage = ref(1)

  const getPosts = function () {
    axios({
      method: 'get',
      url: `${API_URL}/posts/`
    })
      .then(res => {
        // 잘 받아오는지 확인해야함
        console.log(res.data)
        // posts.value = res.data;
        // filteredPosts.value = res.data
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

  return { 
    posts, 
    getPosts, 
    selectedCategory, 
    updateCategory, 
    getFilteredPosts,
    getCurrentCategory,
    currentPage
  }
})