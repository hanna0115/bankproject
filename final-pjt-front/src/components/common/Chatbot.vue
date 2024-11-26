<template>
  <div class="chatbot-container">
    <button 
      @click="toggleChat" 
      class="chat-button"
      :class="{ 'active': isChatOpen }"
    >
      <img src="@/assets/images/salada.png" v-if="!isChatOpen" />
      <XIcon v-else />
    </button>
    
    <Transition name="bounce">
      <div v-if="isChatOpen" class="chat-window">
        <div class="chat-header">
          <img src="@/assets/images/salada.png" alt="" class="salada-icon">
          <h3>Salada</h3>
        </div>
        <div class="chat-messages" ref="messagesContainer">
          <TransitionGroup name="message">
            <!-- v-html을 사용하여 줄바꿈이 포함된 HTML 메시지 렌더링 -->
            <div
              v-for="(message, index) in messages"
              :key="index"
              class="message"
              :class="message.type"
              v-html="message.text"
            ></div>
          </TransitionGroup>
        </div>
        <div class="chat-input">
          <textarea
            v-model="userInput"
            @keyup.enter.exact.prevent="sendMessage"
            @input="adjustTextareaHeight"
            placeholder="질문을 입력해주세요"
            rows="1"
            ref="messageInput"
          ></textarea>
          <button @click="sendMessage" class="send-button" :disabled="!userInput.trim()">
            <SendIcon />
          </button>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, nextTick } from 'vue'
import { SmileIcon, XIcon, SendIcon } from 'lucide-vue-next'
import axios from 'axios'

const isChatOpen = ref(false)
const userInput = ref('')
const messages = ref([
  { type: 'bot', text: '안녕하라다🍊 알고 싶은 금융 지식이 있거나 금융 상품 추천이 필요하면 물어보라다🍊' }
])
const messagesContainer = ref(null)

const toggleChat = () => {
  isChatOpen.value = !isChatOpen.value
}

// 메시지를 Django 서버로 전송하고 응답 받기
const sendMessage = async () => {
  if (userInput.value.trim() === '') return; // 입력 값이 비어있으면 동작하지 않음
  
  // 사용자가 입력한 메시지를 추가
  messages.value.push({ type: 'user', text: userInput.value })

  const inputText = userInput.value // 현재 입력 값을 저장
  userInput.value = '' // 입력창 초기화

  axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/chatbot/',
    data: { user_input: inputText }
  })
    .then((res) => {
      const botReply = res.data.reply // Django에서 이미 <br> 변환된 데이터를 사용
      messages.value.push({ type: 'bot', text: botReply })
    })
    .catch((err) => {
      console.error('Error communicating with chatbot:', err)
      messages.value.push({ type: 'bot', text: '오류가 발생했어요. 다시 시도하라다🍊' })
    })
}
const scrollToBottom = () => {
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  })
}

const randomMovement = () => {
  const button = document.querySelector('.chat-button');
  if (!button || isChatOpen.value) return;
  
  const maxX = window.innerWidth - 100;
  const maxY = window.innerHeight - 100;
  
  const randomX = Math.random() * maxX;
  const randomY = Math.max(window.innerHeight - 200, Math.random() * maxY);
  const randomRotate = Math.random() * 720 - 360; // -360도에서 360도 사이
  
  button.style.transition = 'all 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55)';
  button.style.transform = `translate(${-randomX}px, ${-randomY}px) rotate(${randomRotate}deg) scale(1.2)`;
  
  setTimeout(() => {
    button.style.transform = 'translate(0, 0) rotate(0) scale(1)';
  }, 800);
};

const adjustTextareaHeight = () => {
  const textarea = messageInput.value
  textarea.style.height = 'auto'
  textarea.style.height = textarea.scrollHeight + 'px'
}

watch(messages, scrollToBottom)

onMounted(() => {
  scrollToBottom();
  setInterval(randomMovement, 5000); // 5초마다 실행
})
</script>

<style scoped>
.chatbot-container {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 1000;
  font-family: 'Arial', sans-serif;
  transition: all 0.3s ease;
  perspective: 1000px;
}

.chat-button {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  color: white;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  animation: crazy-bounce 2s cubic-bezier(0.36, 0, 0.66, -0.56) infinite;
  transform-origin: center;
  transform-style: preserve-3d;
  backface-visibility: hidden;
  margin-right: 70px;
  margin-bottom: 30px;
}

.chat-button img {
  width: 70px;
  height: 40px;
}

.chat-button:hover {
  animation: shake-crazy 0.5s cubic-bezier(0.36, 0, 0.66, -0.56) infinite;
}

.chat-button.active {
  animation: none;
  transform: scale(1) rotate(0);
  background-color: #e55a00;
}

@keyframes crazy-bounce {
  0%, 100% {
    transform: translateY(0) rotate(0) scale(1);
  }
  25% {
    transform: translateY(-20px) rotate(15deg) scale(1.1);
  }
  50% {
    transform: translateY(10px) rotate(-15deg) scale(0.95);
  }
  75% {
    transform: translateY(-15px) rotate(5deg) scale(1.05);
  }
}

@keyframes shake-crazy {
  0%, 100% {
    transform: translate(0, 0) rotate(0) scale(1);
  }
  25% {
    transform: translate(10px, -10px) rotate(45deg) scale(1.2);
  }
  50% {
    transform: translate(-15px, 15px) rotate(-30deg) scale(0.8);
  }
  75% {
    transform: translate(15px, 5px) rotate(15deg) scale(1.1);
  }
}

.chat-window {
  position: absolute;
  bottom: 100px;
  right: 0;
  width: 400px;
  height: 500px;
  background-color: white;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.chat-header {
  background-color: #ff6709;
  color: white;
  padding: 15px;
  display: flex;
  align-items: center;
  border-bottom: 2px solid #e55a00;
}

.chat-header h3 {
  margin: 0;
  font-size: 1.2em;
  margin-left: 10px;
}

.salada-icon {
  width: 30px;
}

.header-icon {
  font-size: 1.5em;
}

.chat-messages {
  flex-grow: 1;
  overflow-y: auto;
  padding: 15px;
  background-color: #f8f8ff;
}

.message {
  margin-bottom: 15px;
  padding: 10px 15px;
  border-radius: 18px;
  max-width: 80%;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
  animation: appear 0.3s ease-out;
}

.message.user {
  background-color: #ff6709;
  color: white;
  align-self: flex-end;
  margin-left: auto;
  border-bottom-right-radius: 0;
}

.message.bot {
  background-color: white;
  color: #333;
  align-self: flex-start;
  border-bottom-left-radius: 0;
}

.chat-input {
  display: flex;
  padding: 15px;
  background-color: white;
  border-top: 1px solid #eee;
}

.chat-input textarea {
  flex-grow: 1;
  border: none;
  padding: 10px;
  border-radius: 20px;
  margin-right: 10px;
  background-color: #f0f0f0;
  transition: all 0.3s ease;
  resize: none;
  max-height: 100px;
  overflow-y: auto;
}

.chat-input textarea:focus {
  outline: none;
  box-shadow: 0 0 0 2px #ff6709;
}

.send-button {
  background-color: #ff6709;
  color: white;
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.send-button:hover {
  background-color: #e55a00;
  transform: scale(1.1);
}

.send-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
  transform: none;
}

.bounce-enter-active {
  animation: bounce-in 0.5s;
}
.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1);
  }
}

.message-enter-active,
.message-leave-active {
  transition: all 0.3s ease;
}
.message-enter-from,
.message-leave-to {
  opacity: 0;
  transform: translateY(20px);
}

@keyframes appear {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>