<template>
    <div class="post-body" v-if="post">
        <div class="post-info">
            <p>{{ formatDate(post.created_at) }}  |  조회수 {{ post.num_seen }}</p>
            <button @click="router.push({ name: 'updatePost', params: { postId: post.id } })">수정하기</button>
        </div>
        <div class="content">김선명 (게시물 내용)</div>
        <div class="like">
            <div :class="['like-btn', { 'liked': isLiked }]"
            @click="toggleLike">
            <i class="pi pi-heart-fill"></i>
        </div>
            <p>1</p>
        </div>
    </div>
</template>

<script setup>
import { useCommunityStore } from '@/stores/community';
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const router = useRouter()
const route = useRoute()
const communityStore = useCommunityStore()
const userStore = useUserStore()

defineProps({
    post: Object
})

// const checkAndUpdatePost = function () {
//     const currentUserId = userStore.userId; // 현재 로그인한 사용자 ID
//     const postAuthorId = communityStore.post.authorId; // 게시글 작성자 ID (가정)

//     if (currentUserId !== postAuthorId) {
//         alert("이 게시글은 당신이 작성한 것이 아닙니다. 로그인 페이지로 이동합니다.");
//         router.push({ name: 'login' }); // 로그인 페이지로 이동
//     } else {
//         updatePost(); // 수정 요청 진행
//     }
// };

const formatDate = (dateString) => {
    const date = new Date(dateString);
    return `${date.getFullYear()}.${String(date.getMonth() + 1).padStart(2, '0')}.${String(date.getDate()).padStart(2, '0')}`;
}

const isLiked = ref(false);
const likeCount = ref(1);

const getLiked = function () {
    axios({
        method: 'post',
        url: `${communityStore.API_URL}/like_post/${route.params.id}/`
    })
        .then(res => {
            // 좋아요 되어 있으면 isLiked true로 바꾸기
            // 좋아요 개수 가져오기(likeCount)
        })
        .catch(err => console.log('좋아요 시 오류', err))
}

const toggleLike = () => {
  isLiked.value = !isLiked.value;
  if (isLiked.value) {
    likeCount.value++;
  } else {
    likeCount.value--;
  }
}

onMounted(() => {
    // getLiked()
})
</script>

<style scoped>
.post-body {
    margin: 10px 0;
}

.post-info {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
}

.post-info button {
    text-decoration: underline;
    cursor: pointer;
}

.content {
    margin: 30px 0;
}

.like {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    margin: 10px;
}

.like-btn {
    margin-right: 5px;
    margin-bottom: 5px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-size: 24px;
}

.like-btn i {
    font-size: 16px;
    color: #bcbcbc;
}

.like-btn.liked i {
    color: crimson;
    animation: pulse 500ms ease;
}

/* 좋아요 버튼 눌렀을 때 크기 변하는 애니메이션 */
@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}
</style>