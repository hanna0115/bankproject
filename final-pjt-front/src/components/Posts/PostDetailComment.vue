<template>
    <div class="comments">
        <p>댓글</p>
        <form @submit.prevent="userStore.isLoggedIn ? createComment() : router.push({ name: 'login' })">
            <input type="text" placeholder="댓글을 입력하세요" v-model="content">
            <button>작성하기</button>
        </form>
        <div class="comment-ilst">
            <div class="comment-item" v-for="comment in comments" :key="comment.id">
                <div class="comment-info">
                    <p>{{ comment.name }}</p>
                    <span>|</span> 
                    <p class="comment-content">{{ comment.content }}</p>
                </div>
                
                <p @click="deleteComment(comment.id)" class="comment-delete"
                v-if="userStore.isLoggedIn && userStore.user.pk == comment.user">댓글삭제</p>
            </div>
            <p class="no-comment" v-if="!comments.length">작성된 댓글이 없습니다.</p>
        </div>
    </div>
</template>

<script setup>
import { useCommunityStore } from '@/stores/community';
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { ref, onMounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute()
const router = useRouter()
const communityStore = useCommunityStore()
const userStore = useUserStore()

const props = defineProps({
    post: Object
})

console.log(props.post.comment_set)
const content = ref(null)
const comments = ref([])

// 댓글 생성
const createComment = function () {
    axios({
        method: 'post',
        url: `${communityStore.API_URL}/posts/${route.params.postId || 1}/comments/`,
        data: {
            content: content.value
        },
        headers: {
            Authorization: `Token ${userStore.token}`
        }
    })
        .then(res => {
            console.log('댓글 생성 완료')
            comments.value.push(res.data)
            content.value = ''
        })
        .catch(err => console.log('댓글 생성 실패', err))
}

// 댓글 삭제
const deleteComment = function (commentId) {
    axios({
        method: 'delete',
        url: `${communityStore.API_URL}/posts/delete_comment/${commentId}/`,
        headers: {
            Authorization: `Token ${userStore.token}`
        }
    })
        .then(res => {
            comments.value = comments.value.filter(comment => comment.id !== commentId)
        })
        .catch(err => console.log('댓글 삭제 실패', err))
}

// 댓글 목록 업데이트 함수
const updateComments = () => {
    if (communityStore.post && communityStore.post.comment_set) {
        comments.value = communityStore.post.comment_set;
    }
}

// route.params.postId가 변경될 때마다 댓글 목록 업데이트
watch(() => route.params.postId, async (newPostId) => {
    if (newPostId) {
        await communityStore.getPostDetail(newPostId);
        updateComments();
    }
});

onMounted(() => {
    updateComments();
})
</script>

<style scoped>
.comments {
    margin: 10px;
    font-weight: bold;
}

.comments > p {
    margin-left: 10px;
}

.comments form {
    position: relative
}

.comments input[type="text"] {
    width: 100%;
    padding: 8px;
    padding-right: 15%;
    border: none;
    border-radius: 6px;
    margin-top: 10px;
}

.comments button {
    position: absolute;
    top: 16px;
    right: 6px;
    padding: 3px 10px;
    font-size: 12px;
    color: #fff;
    background-color: #ff9966;
    border-radius: 20px;
}

.comments button:hover {
    background-color: #ff8855;
}

.comment-item {
    display: flex;
    justify-content: space-between;
    margin: 15px 10px;
    font-size: 14px;
}

.comment-info {
    display: flex;
}

.comment-info span {
    margin: 0 10px;
}


.comment-delete {
    cursor: pointer;
    width: 50px;
    text-decoration: underline;
    text-align: end;
    word-break: keep-all;
}

.no-comment {
    margin-top: 25px;
    text-align: center;
}
</style>