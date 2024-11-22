<template>
    <div class="comments">
        <p>댓글</p>
        <form @submit.prevent="userStore.isLoggedIn ? createComment() : router.push({ name: 'login' })">
            <input type="text" placeholder="댓글을 입력하세요" v-model="content">
            <button>작성하기</button>
        </form>
        <div class="comment-ilst" v-if="comments">
            <div class="comment-item" v-for="comment in comments" :key="comment.id">
                <div class="comment-info">
                    <p>{{ comment.user.name }}</p>
                    <span>|</span> 
                    <p class="comment-content">{{ comment.content }}</p>
                </div>
                
                <p @click="deleteComment(comment.id)" class="comment-delete"
                v-if="userStore.isLoggedIn && userStore.user.pk == comment.user.id">댓글삭제</p>
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
            console.log('댓글 생성 완료');
        
        // 새로 생성된 댓글을 기존 댓글 형식에 맞게 변환
        const newComment = {
            id: res.data.id,
            content: res.data.content,
            created_at: res.data.created_at,
            updated_at: res.data.updated_at,
            user: {
                name: userStore.user.name, // 현재 로그인한 유저의 이름
                id: userStore.user.pk // 현재 로그인한 유저의 PK
            }
        };
        
        comments.value.push(newComment); // 변환된 댓글을 추가
        content.value = ''; // 입력 필드 초기화
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
        console.log(communityStore.post)
    }
}

// route.params.postId가 변경될 때마다 댓글 목록 업데이트
watch(() => route.params.postId, async (newPostId) => {
    // newPostId가 존재하지 않을 때 기본 게시글 ID인 1번 게시글의 댓글 목록을 가져오기
    const postIdToFetch = newPostId || 1; // newPostId가 없으면 1로 설정

    // 해당 게시글의 상세 정보를 가져옵니다.
    await communityStore.getPostDetail(postIdToFetch);
    
    // 댓글 목록 업데이트
    updateComments()
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