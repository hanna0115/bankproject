<template>
    <div class="post-detail-container">
        <div class="post-header">
            <h2>돈 모으는 꿀팁 알려줄까</h2>
            <p>user-name</p>
        </div>

        <hr>
        <div class="post-body">
            <div class="post-info">
                <p>작성일 2024.11.01 | 조회수 13</p>
                <p>수정하기</p>
            </div>
            <div class="content">김선명 (게시물 내용)
            </div>
            <div class="like">
                <div class="like-btn">♡</div>
                <p>1</p>
            </div>
        </div>

        <hr>
        <div class="comments">
            <p>댓글</p>
            <form>
                <input type="text" placeholder="댓글을 입력하세요">
                <button>작성</button>
            </form>
        </div>
        <div class="comment-list">
            <div>
                <span>user-name | 댓글 내용</span>
                <span class="comment-delete">댓글 삭제</span>
            </div>
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>
.post-detail-container {
    width: 60%;
    margin-left: 30px;
    padding: 20px;
    background-color: #F9FAFB;
    border-radius: 8px;
}

.post-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    margin: 10px 0;
}

.post-header h2 {
    color: #333;
    font-size: 24px;
}

.post-header p {
    color: #565656;
    font-size: 16px;
}

hr {
    border-top: 1px solid #bcbcbc;
}

.post-body {
    margin: 10px 0;
}

.post-info {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
}

.content {
    height: 200px;
    margin: 30px 0;
    overflow-y: auto;
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