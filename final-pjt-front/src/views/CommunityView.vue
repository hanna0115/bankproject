<template>
    <div class="container">
        <h2>커뮤니티</h2>

        <div class="community-nav">
            <div class="category">
                <p>카테고리</p>
                <div v-for="category in categories"
                    :key="category.value"
                    class="category-item">
                    <input type="radio" :id="category.id" :value="category.value"
                        v-model="communityStore.getCurrentCategory"
                        @change="updateCategory(category.value)"
                        class="hidden-radio">
                    <label :for="category.id" class="category-label">{{ category.label }}</label>
                </div>
            </div>
            <button @click="router.push(userStore.isLoggedIn ? { name: 'createPost' } : { name: 'login' })" class="write-btn">작성하기</button>
        </div>
        
        <div class="content-wrapper">
            <PostList
            :post-list="communityStore.getFilteredPosts"/>
            <PostDetail />
        </div>
    </div>
</template>

<script setup>
import { useCommunityStore } from '@/stores/community';
import { useUserStore } from '@/stores/user';
import PostList from '@/components/Posts/PostList.vue';
import PostDetail from '@/components/Posts/PostDetail.vue';
import { onMounted } from 'vue';
import router from '@/router';

const communityStore = useCommunityStore()
const userStore = useUserStore()

const categories = [
    { id: 'all', value: 'all', label: '전체' },
    { id: 'account', value: 'account', label: '예적금' },
    { id: 'asset', value: 'asset', label: '부동산' },
    { id: 'stock', value: 'stock', label: '주식' },
    { id: 'etc', value: 'etc', label: '기타' },
];


const updateCategory = (category) => {
    communityStore.updateCategory(category);
};

onMounted(() => {
    communityStore.getPosts()
})
</script>

<style scoped>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    max-width: 1280px;
    margin: 0 auto 100px;
    padding: 0 20px;
    overflow: hidden;
}

.container h2 {
    margin: 100px auto 65px;
    color: #FF6708;
}

.community-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-bottom: 10px;
}

.category {
    display: flex;
}

.category p {
    margin-right: 20px;
}

.category p,
.category div {
    padding: 10px 5px;
    font-size: 18px;
}

.category p,
.category label {
    cursor: pointer;
}

.category label {
    padding: 3px 10px;
    border-radius: 20px;
}

.category-label:hover {
    background-color: #e9ecef;
}

.category p:first-child {
    color: #FF6708;
    cursor: default;
}

.category input {
    display: none;
}

.category input:checked + .category-label {
    background-color: #FF6708;
    color: white;
    border-color: #FF6708;
    transition: all 0.3s ease-in-out;
}


.write-btn {
    padding: 8px 20px;
    background-color: #ff9966;
    color: white;
    border: none;
    border-radius: 30px;
    cursor: pointer;
}

.write-btn:hover {
    background-color: #ff8855;
}

.content-wrapper {
    display: flex;
    justify-content: center;
    width: 100%;
    height: 100%;
}
</style>