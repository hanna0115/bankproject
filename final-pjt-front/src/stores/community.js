import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useCommunityStore = defineStore("community", () => {
  const url = 'http://127.0.0.1:8000'
  const posts = ref([])
  const filteredPosts = ref([])

  const getPosts = function () {
    axios({
      method: 'get',
      url: `${url}/posts/`
    })
      .then(res => {
        console.log(res.data)
        posts.value = res.data
      })
      .catch(err => console.log(err))
  }

  const filterPost = function () {

  }
  
  return { posts, getPosts };
});
