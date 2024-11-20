<template>
    <div class="comments">
        <p>댓글</p>
        <form>
            <input type="text" placeholder="댓글을 입력하세요" v-model="content">
            <button @click="createComment">작성하기</button>
        </form>
        <div class="comment-ilst">
            <div class="comment-item" v-for="comment in comments">
                <div class="comment-info">
                    <p>user-name</p>
                    <span>|</span> 
                    <p class="comment-content">댓글 내용</p>
                </div>
                <p @click="deleteComment(comment.id)" class="comment-delete">댓글삭제</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useCommunityStore } from '@/stores/community';
import axios from 'axios';
import { ref } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute()
const store = useCommunityStore()

const content = ref(null)
const comments = ref([])

// 댓글 목록 불러오기
const fetchComments = function () {
    axios({
        method: 'get',
        url: `${store.API_URL}/detail/${route.params.id}/`
    })
        .then(res => {
            comments.value = res.data
        })
        .catch(err => console.log('댓글 불러오기 실패', err))
}

// 댓글 생성 및 목록 업데이트
const createComment = function () {
    axios({
        method: 'post',
        url: `${store.API_URL}/${route.params.id}/comments/`,
        data: {
            content: content.value
        }
    })
        .then(res => {
            comments.value.push({
            userName: 'user-name', // 사용자 이름은 실제 데이터로 대체해야 함
            content: res.data.content // 서버에서 반환된 댓글 내용
        })
        })
        .catch(err => console.log('댓글 생성 실패', err))
}

// 댓글 삭제
const deleteComment = function (commentId) {
    axios({
        method: 'delete',
        url: `${store.API_URL}delete_comment/${commentId}/`,
    })
        .then(res => {
            comments.value = comments.value.filter(comment => comment.id !== commentId)
        })
        .catch(err => console.log('댓글 삭제 실패', err))
}

// onMounted(() => {
//     fetchComments()
// })
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

.comment-content {
    max-width: 60%;
}

.comment-delete {
    cursor: pointer;
    width: 50px;
    text-decoration: underline;
    text-align: end;
    word-break: keep-all;
}
</style>