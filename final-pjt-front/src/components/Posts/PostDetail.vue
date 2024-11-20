<template>
    <div class="post-detail-container">
        <div class="post-header">
            <h2>돈 모으는 꿀팁 알려줄까</h2>
            <p>user-name</p>
        </div>

        <hr>
        <PostDetailBody/>
        <hr>
        <PostDetailComment/>

    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import PostDetailBody from '@/components/Posts/PostDetailBody.vue';
import PostDetailComment from '@/components/Posts/PostDetailComment.vue';
import { useCommunityStore } from '@/stores/community';
const router = useRouter()

const store = useCommunityStore()
const route = useRoute()

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