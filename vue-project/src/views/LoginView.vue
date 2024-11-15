<template>
    <div class="login">
        <h2 class="title">Welcome to</h2>

        <form>
            <div class="id">
                <label for="id">아이디</label>
                <input type="text" id="id" placeholder="example@email.com">
            </div>
            <div class="password">
                <label for="password">비밀번호</label>
                <input type="password" id="password" placeholder="********">
            </div>
            <input type="submit" value="로그인">
        </form>

        <div class="user-nav">
            <p>회원가입</p>
            <span> | </span>
            <p>아이디 찾기</p>
            <span> | </span>
            <p>비밀번호 찾기</p>
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>
.login {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin-top: 150px;
}

.login .title {
  color: #FF6709;
  font-weight: bold;
  font-size: 30px;
}

form {
    width: 350px;
    margin-top: 60px;
}

form div {
    display: flex;
    justify-content: center;
    flex-direction: column;
    margin: 15px 0;
}

form label {
    margin-bottom: 5px;
    font-weight: 700;
    color: #FFB07E;
}

form input {
    width: 100%;
    padding: 10px 0;
    border: none;
    border-bottom: 1.35px solid #909090;
}

form input:focus {
    outline: none;
}

form input[type='submit'] {
  background-color: rgba(255,103,8,0.6);
  color: white;
  margin-top: 30px;
  padding: 10px 12px; 
  font-weight: 700;
  font-size: 16px;
  border: none;
  border-radius: 30px;
}
</style>