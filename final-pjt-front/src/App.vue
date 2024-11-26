<template>
  <Nav />
  <RouterView />
  <Chatbot />
</template>

<script setup>
import { RouterView } from 'vue-router'
import Nav from '@/components/common/Nav.vue';
import Chatbot from './components/common/Chatbot.vue';
</script>

<style scoped>

</style>