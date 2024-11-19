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
                <button>작성하기</button>
            </form>
            <div class="comment-ilst">
                <div class="comment-item">
                    <div class="comment-info">
                        <p>user-name</p>
                        <span>|</span> 
                        <p class="comment-content">댓글 내용</p>
                    </div>
                    <p class="comment-delete">삭제</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>
.post-detail-container {
    width: 60%;
    max-height: 625px;
    margin-left: 30px;
    padding: 20px;
    background-color: #F9FAFB;
    border-radius: 8px;
    overflow-y: auto;
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

.post-info p:last-child {
    text-decoration: underline;
}

.content {
    margin: 30px 0;;
}

.like {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    margin: 10px;
}

.like-btn {
    margin-right: 5px;
}

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
    word-break: keep-all;
}
</style>