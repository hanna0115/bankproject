<template>
    <div class="post-detail-container" v-if="store.post">
        <div class="post-header">
            <h2>{{ store.post.title }}</h2>
            <p>{{ store.post.name }}</p>
        </div>

        <hr>
        <PostDetailBody :post="store.post"/>
        <hr>
        <PostDetailComment :post="store.post"/>
    </div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useCommunityStore } from '@/stores/community';
import PostDetailBody from '@/components/Posts/PostDetailBody.vue';
import PostDetailComment from '@/components/Posts/PostDetailComment.vue';
import { storeToRefs } from 'pinia';


const store = useCommunityStore();
const route = useRoute();

// postId에 따라 게시글 정보를 가져오는 watch 설정
// postId가 변경될 때마다 getPostDetail 호출
watch(() => route.params.postId, (newPostId) => {
    if (newPostId) {
        store.getPostDetail(newPostId);
    }
});

// 컴포넌트가 마운트될 때 초기 게시글 정보 가져오기
onMounted(() => {
    store.getPostDetail(1);
});

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