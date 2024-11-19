<!-- CommunityView.vue -->
<template>
    <div class="container">
        <h2>커뮤니티</h2>
        <div class="category">
            <p>카테고리</p>
            <p>전체</p>
            <p>예적금</p>
            <p>부동산</p>
            <p>주식</p>
            <p>기타</p>
        </div>

        <div class="content-wrapper">
            <PostList />
            <PostDetail />
        </div>
    </div>
</template>

<script setup>
import PostList from '@/components/PostList.vue';
import PostDetail from '@/components/PostDetail.vue';
</script>

<style scoped>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 20px;
    overflow: hidden;
}

.container h2 {
    margin: 100px auto 65px;
    color: #FF6708;
}


.category {
    display: flex;
    align-self: start;
}

.category p {
    padding: 10px;
    font-size: 18px;
}

.category p:first-child {
    color: #FF6708;
}

.content-wrapper {
    display: flex;
    justify-content: center;
    width: 100%;
    height: 100%;
}

</style>