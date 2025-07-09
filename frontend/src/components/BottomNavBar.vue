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
    <button @click="goTo('/admin')" class="flex-1 text-center">
      <div>🛠️</div>
      <div class="text-xs">Админ</div>
    </button>
    <!-- <button
      v-if="isAdmin"
      @click="goTo('/admin')"
      class="flex flex-col items-center text-sm text-red-500"
    >
      <span>🛠️</span>
      <span>Админ</span>
    </button> -->
  </nav>
</template>




<script setup>
import { useRouter } from 'vue-router'
import { ADMIN_IDS } from '../constants/admins'
import { useWorkoutStore } from '../stores/workoutStore'

const store = useWorkoutStore()
const router = useRouter()
const isAdmin = ADMIN_IDS.includes(store.telegramId)


const goTo = (path) => {
  router.push(path)
}



</script>