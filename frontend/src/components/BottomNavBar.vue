<template>
  <nav class="fixed bottom-0 left-0 right-0 bg-white border-t shadow-inner flex justify-around py-2 z-50">
    <button @click="goTo('/')" class="flex-1 text-center">
      <div>🏋️‍♂️</div>
      <div class="text-xs">Тренировки</div>
    </button>
    <button @click="goTo('/stats')" class="flex-1 text-center">
      <div>📊</div>
      <div class="text-xs">Статистика</div>
    </button>
    <button @click="goTo('/programs')" class="flex-1 text-center">
      <div>📋</div>
      <div class="text-xs">Программы</div>
    </button>
  </nav>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

const goTo = (path) => {
  router.push(path)
}
</script>