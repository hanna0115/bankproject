<template>
    <div class="board-container">
        <div class="post-list">
            <p v-if="!postList.length" class="no-post">작성된 게시물이 없습니다.</p>
            <div v-for="(post, index) in paginatedPosts" :key="post.id" class="post-item">
                    <RouterLink :to="{ name: 'postdetail', params: { postId: post.id} }"
                    @click="clickPost(post.id)">
                    <div class="post-body">
                        <p class="post-number">{{ startIndex + index + 1 }}/</p>
                        <div class="post-content">
                            <span class="user-id">{{ post.userId }}</span>
                            <h3 class="post-title">{{ post.title }}</h3>
                        </div>
                    </div>
                    <div class="post-footer">
                        <span class="post-date">작성일 {{ store.formatDate(post.created_at) }}</span> | <span class="post-views">조회 {{ post.num_seen }}</span>
                    </div>
                </RouterLink>
                </div>
        </div>
        <div class="pagination">
            <button @click="goToPage(store.currentPage - 1)" :disabled="store.currentPage === 1">이전</button>
            <button 
                v-for="pageNumber in displayedPageNumbers" 
                :key="pageNumber" 
                @click="goToPage(pageNumber)"
                :class="{ active: store.currentPage === pageNumber }"
            >
                {{ pageNumber }}
            </button>
            <button @click="goToPage(store.currentPage + 1)" :disabled="store.currentPage === totalPages">다음</button>
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue';
import { RouterLink, useRouter, onBeforeRouteUpdate } from 'vue-router';
import { useCommunityStore } from '@/stores/community'; // store import 추가

const router = useRouter();
const store = useCommunityStore(); // store 사용

const props = defineProps({
    postList: Array
});

// 페이지네이션
const postsPerPage = 5;
const totalPages = computed(() => Math.ceil(props.postList.length / postsPerPage));
const startIndex = computed(() => (store.currentPage - 1) * postsPerPage);

const paginatedPosts = computed(() => {
    const start = startIndex.value;
    return props.postList.slice(start, start + postsPerPage);
});

const displayedPageNumbers = computed(() => {
    const pageNumbers = [];
    let startPage = Math.max(1, store.currentPage - 2);
    let endPage = Math.min(totalPages.value, startPage + 4);
    
    if (endPage - startPage < 4) {
        startPage = Math.max(1, endPage - 4);
    }

    for (let i = startPage; i <= endPage; i++) {
        pageNumbers.push(i)
    }

    return pageNumbers
});

const goToPage = (page) => {
    if (page >= 1 && page <= totalPages.value) {
        store.currentPage = page; // store의 currentPage 업데이트
    }
}

// 클릭할 때, params의 id를 넘겨주기
const clickPost = (postId) => {
    store.getPostDetail(postId)
}

</script>

<style scoped>
.board-container {
    display: flex;
    flex-direction: column;
    width: 40%;
    /* max-width 제거하고 width 100%로 설정 */
}

.no-post {
    margin: 50px 0;
    text-align: center;
}

.post-list {
    width: 100%;
}

.post-item {
    background-color: #F9FAFB;
    border-radius: 8px;
    margin-bottom: 10px;
    padding: 20px;
    cursor: pointer;
}

.post-body {
    display: flex;
    align-items: center;
}

.post-number {
    margin-right: 10px;
    font-size: 28px;
    color: #ff8940;
}

.post-content {
    font-weight: bold;
}

.user-id {
    color: #666;
    font-size: 14px;
}

.post-title {
    font-size: 18px;
    margin: 0;
    color: #333;
}

.post-footer {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    margin-top: 10px;
    font-size: 12px;
    color: #888;
}

.post-item:hover {
    background-color: #f0f0f0;
}

.pagination {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
}

.pagination button {
    padding: 5px 10px;
    margin: 0 5px;
    background-color: #fff;
    color: #333;
    border: 1px solid #ddd;
    border-radius: 5px;
    cursor: pointer;
}

.pagination button:disabled {
    color: #ccc;
    cursor: not-allowed;
}

.pagination button.active {
    background-color: #ff8940;
    color: white;
    border-color: #ff8940;
}

.pagination button:hover:not(:disabled) {
    background-color: #f0f0f0;
}
</style>