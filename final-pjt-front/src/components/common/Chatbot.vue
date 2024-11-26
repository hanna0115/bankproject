<template>
  <div class="chatbot-container">
    <button 
      @click="toggleChat" 
      class="chat-button"
      :class="{ 'active': isChatOpen }"
    >
      <SmileIcon v-if="!isChatOpen" />
      <XIcon v-else />
    </button>
    
    <Transition name="bounce">
      <div v-if="isChatOpen" class="chat-window">
        <div class="chat-header">
          <SmileIcon class="header-icon" />

          <h3>Cute Chatbot</h3>
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

  // Simulate bot response (replace with actual chatbot logic)
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

watch(messages, scrollToBottom)

onMounted(scrollToBottom)
</script>

<style scoped>
.chatbot-container {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 1000;
  font-family: 'Arial', sans-serif;
}

.chat-button {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background-color: #ff6709;
  color: white;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 15px rgba(255, 103, 9, 0.4);
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.chat-button:hover {
  transform: scale(1.1) rotate(5deg);
}

.chat-button.active {
  background-color: #e55a00;
  transform: scale(1.1) rotate(-5deg);
}

.chat-window {
  position: absolute;
  bottom: 80px;
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

