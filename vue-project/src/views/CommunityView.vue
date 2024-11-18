<!-- CommunityView.vue -->
<template>
    <div class="container">
        <div class="content-wrapper">
            <div class="post-list">
                <PostList/>
            </div>
            <div class="post-detail">
                <PostDetail/>
            </div>
        </div>
    </div>
</template>

<script setup>
import PostList from '@/components/PostList.vue';
import PostDetail from '@/components/PostDetail.vue';
</script>

<style scoped>
.container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 20px;
    height: 100%;
    overflow: hidden;
}

.content-wrapper {
    display: flex;
    height: 100%;
    gap: 30px; /* 간격 추가 */
}

.post-list {
    flex: 0 0 500px; /* 고정 너비 500px 설정 */
    /* overflow-y: auto; */
}

.post-detail {
    flex: 1; /* 남은 공간 모두 차지 */
    /* overflow-y: auto; */ /* 디테일 스크롤바
    padding-left: 30px; /* 왼쪽 여백 추가 */

}
</style>