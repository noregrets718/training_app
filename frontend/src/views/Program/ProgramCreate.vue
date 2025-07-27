<template>
  <div class="max-w-xl mx-auto p-6 bg-white rounded shadow">
    <h2 class="text-xl font-semibold mb-4">Создание программы</h2>
    <input v-model="title" type="text" placeholder="Название программы" class="input mb-2" />
    <textarea v-model="description" placeholder="Описание программы" class="input h-24 mb-4" />
    <button @click="goNext" class="bg-blue-600 text-white px-4 py-2 rounded">Далее</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const title = ref('')
const description = ref('')
const router = useRouter()

const goNext = () => {
  // сохранить title/description (например, в store или отправить сразу)
  router.push('/programs/edit/1') // заменишь ID на реальный
}
</script>

<style scoped>
.input {
  @apply w-full border border-gray-300 rounded px-3 py-2;
}
</style>