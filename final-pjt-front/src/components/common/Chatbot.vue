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
            <div v-for="(message, index) in messages" :key="index" class="message" :class="message.type">
              {{ message.text }}
            </div>
          </TransitionGroup>
        </div>
        <div class="chat-input">
          <input 
            v-model="userInput" 
            @keyup.enter="sendMessage" 
            placeholder="Type a message..."
          />
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

const isChatOpen = ref(false)
const userInput = ref('')
const messages = ref([
  { type: 'bot', text: 'Hi there! How can I help you today? 😊' }
])
const messagesContainer = ref(null)

const toggleChat = () => {
  isChatOpen.value = !isChatOpen.value
}

const sendMessage = () => {
  if (userInput.value.trim() === '') return

  messages.value.push({ type: 'user', text: userInput.value })
  userInput.value = ''

  setTimeout(() => {
    messages.value.push({ type: 'bot', text: "That's interesting! I'm a cute chatbot, but I'm still learning. Can you tell me more? 🌟" })
  }, 1000)
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
  width: 300px;
  height: 400px;
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

.chat-input input {
  flex-grow: 1;
  border: none;
  padding: 10px;
  border-radius: 20px;
  margin-right: 10px;
  background-color: #f0f0f0;
  transition: all 0.3s ease;
}

.chat-input input:focus {
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