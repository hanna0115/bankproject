<template>
    <div class="board-container">
        <h2 class="board-title">전체 게시글</h2>
        
        <div class="post-list">
            <div v-for="n in 5" :key="n" class="post-item">
                <div class="post-body">
                    <p class="post-number">1/</p>
                    <div class="post-content">
                        <span class="user-id">미마마</span>
                        <h3 class="post-title">돈 모으는 꿀팁 알려줄까</h3>
                    </div>
                </div>
                <div class="post-footer">
                    <span class="post-date">작성일 2024.11.01</span> | <span class="post-views">조회 11</span>
                </div>
            </div>
        </div>
        <button @click="router.push('/createpost')"
        class="write-btn">작성하기</button>
    </div>
</template>

<script setup>

import { useRouter } from 'vue-router';

const router = useRouter();

</script>

<style scoped>
.board-container {
    position: relative;
    width: 100%; /* max-width 제거하고 width 100%로 설정 */
    padding: 0px;
    top: 17px;
}


.board-title {
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 40px;
    color: #ff8940;
}

.post-list {
    display: flex;
    flex-direction: column;
    gap: 15px;
    padding: 0px;
    width: 100%; /* 고정 너비 제거 */
}

.post-item {
    position: relative;
    background-color: #F9FAFB;
    border-radius: 8px;
    padding: 20px;
    cursor: pointer;
    top: 20px;
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
    gap: 15px;
    margin-top: 10px;
    font-size: 12px;
    color: #888;
}

.write-btn {
    position: relative;
    float: right;
    margin-top: 20px;
    padding: 8px 20px;
    background-color: #ff9966;
    color: white;
    border: none;
    border-radius: 30px;
    cursor: pointer;
    top: 15px;
}

.write-btn:hover {
    background-color: #ff8855;
}

.post-item:hover {
    background-color: #f0f0f0;
}
</style>