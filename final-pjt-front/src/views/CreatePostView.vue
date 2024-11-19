<template>
    <div class="container">
        <h2 class="title">게시글 작성하기</h2>
        <div class="main">
            <span class="category">* 카테고리를 선택하세요</span>
            <div class="tag">
                <span 
                    :class="['account', { active: selectedTag === 'account' }]"
                    @click="selectTag('account')"
                >예적금</span>
                <span 
                    :class="['asset', { active: selectedTag === 'asset' }]"
                    @click="selectTag('asset')"
                >부동산</span>
                <span 
                    :class="['stock', { active: selectedTag === 'stock' }]"
                    @click="selectTag('stock')"
                >주식</span>
                <span 
                    :class="['etc', { active: selectedTag === 'etc' }]"
                    @click="selectTag('etc')"
                >기타</span>
            </div>
        </div>

        <form class="post">
            <div class="input-group">
                <label for="post-title" class="post-title">제목</label>
                <input type="text" id="post-title">
            </div>
            <div class="input-group">
                <label for="post-content" class="post-content">내용</label>
                <textarea name="post-content" id="post-content" class="post-textarea"></textarea>
            </div>
        </form>
        <button @click="router.push('/community')"
        class="post-btn">작성하기</button>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()


const selectedTag = ref('');

const selectTag = (tag) => {
    selectedTag.value = tag;
};



</script>

<style scoped>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin-top: 50px;
    width: 100%;
    max-width: 800px;
    margin: 50px auto;
}

.title {
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 30px;
    text-align: center;
}

.main {
    width: 100%;
    margin-bottom: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.category {
    font-size: 16px;
    display: block;
    margin-bottom: 15px;
    text-align: center;
    font-size: 12px;
    color: #888;
}

.tag {
    display: flex;
    gap: 15px;
    justify-content: center;
    align-items: center;
    height: 30px;
}

.tag span {
    padding: 8px 25px;
    /* border: 1px solid #FF6709; */
    color: #888;
    border-radius: 20px;
    font-size: 18px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-size: 12px;
}

.tag span.active {
    background-color: #FFB07E;
    color: white;
}

.post {
    width: 100%;
}

.input-group {
    margin-bottom: 20px;
    width: 100%;
    
}

.input-group label {
    position: relative;
    display: block;
    margin-bottom: -11px;
    font-size: 16px;
    z-index: 1px;
    background-color: white;
    width: 40px;
    text-align: center;
    left: 15px;
}

.input-group input,
.input-group textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    outline: none;
}

.input-group input {
    height: 40px;
}

.input-group textarea {
    height: 600px;
    resize: none;
}


.post-btn {
    background-color: #FF6708;
    color: white;
    border: none;
    padding: 12px 30px;
    border-radius: 20px;
    font-size: 16px;
    cursor: pointer;
    margin-top: 20px;
}

.post-btn:hover {
    background-color: #e55a00;
}
</style>

