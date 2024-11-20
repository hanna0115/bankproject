<template>
    <div class="post-detail-container"  v-if="post">
        <div class="post-header">
            <h2>{{ post.title }}</h2>
            <p>{{ post.name }}</p>
        </div>

        <hr>
        <PostDetailBody/>
        <hr>
        <PostDetailComment/>

    </div>
</template>

<script setup>
import { onMounted, onUpdated, ref } from 'vue';
import { onBeforeRouteUpdate, useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import { useCommunityStore } from '@/stores/community';
import PostDetailBody from '@/components/Posts/PostDetailBody.vue';
import PostDetailComment from '@/components/Posts/PostDetailComment.vue';
import { storeToRefs } from 'pinia';

const store = useCommunityStore()
const router = useRouter()
const route = useRoute()
const post = storeToRefs(store.post)
const postNum = ref(1)

// 단일 게시글 조회
onMounted(() => {
    store.getPostDetail(postNum.value)
})

onUpdated(() => {
    store.getPostDetail(router.params.postId)
})

onBeforeRouteUpdate((to, from) => {
    // console.log(post)
    post.value = store.post
    // console.log(post)
})


</script>

<style scoped>
.post-detail-container {
    width: 60%;
    max-height: 625px;
    margin-left: 30px;
    padding: 20px;
    background-color: #F9FAFB;
    border-radius: 8px;
    overflow-y: auto;
}

.post-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    margin: 10px 0;
}

.post-header h2 {
    color: #333;
    font-size: 24px;
}

.post-header p {
    color: #565656;
    font-size: 16px;
}

hr {
    border-top: 1px solid #bcbcbc;
}
</style>