<template>
    <div class="container">
        <h2>돈 모으는 꿀팁 알려줄까</h2>
        <span>닉네임</span>
        <hr>
        <span>작성일 2024.11.01</span> | <span>조회수 13</span>
        <div class="content">
            <span>
                김선명
            </span>
        </div>
        <hr>
        <div>
            <p>댓글</p>
            <form>
                <input type="text">
                <button class="write">작성</button>
            </form>
        </div>
        <div class="comment">
            <p>오한나 <span> | </span> 좋아요
                <span class="comment-delete">삭제</span>
            </p>
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>
.container {
    position: relative;
    padding: 20px;
    width: calc(100% - 40px); /* 패딩 고려한 너비 설정 */
    font-size: 12px;
    right: 10px;
    top: 132px;
    background-color: #F9FAFB;
    border-radius: 8px;
}


h2 {
    color: #333;
    margin-bottom: 10px;
}

.content {
    width: 90%;
    min-height: 200px;
    /* padding: 10px; */
    border-radius: 4px;
    resize: none;
    margin: 30px 0;
}

hr {
    border: none;
    border-top: 1px solid #eee;
    margin: 15px 0;
}

input[type="text"] {
    width: 90%;
    padding: 8px;
    border: 1px solid #eee;
    border-radius: 4px;
    margin-top: 10px;
}


.write {
    position: relative;
    right: 35px;
}

.comment {
    cursor: pointer;
    margin-top: 30px;
}

.comment-delete {
    cursor: pointer;
    position: relative;
    left: 499px;
}

button:hover {
    background-color: #ff8855;
}
</style>