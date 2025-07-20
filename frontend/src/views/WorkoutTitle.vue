<template>
  <div class="p-6 max-w-md mx-auto bg-white rounded-lg shadow-md">
    <h1 class="text-2xl font-semibold mb-4 text-gray-900">Название тренировки</h1>

    <input
      v-model="title"
      placeholder="Например: Грудь/бицепс"
      class="w-full p-3 mb-4 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
      @input="autoSaveTitle"
    />

    <button
      @click="goToExerciseSelect"
      :disabled="!title"
      class="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg py-3"
    >
      Продолжить
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue'
import { useRouter} from 'vue-router'
import { useWorkoutStore } from '../stores/workoutStore'
import { useNavigationStore } from '../stores/navigationStore'
import axios from 'axios'

const title = ref('')
const router = useRouter()
const store = useWorkoutStore()
const nav = useNavigationStore()
const telegramId = store.telegramId
const BASE_SITE = inject("BASE_SITE");

const autoSaveTitle = async () => {
  if (!telegramId) return
  await axios.post(`${BASE_SITE}/workouts/users/${store.telegramId}/unfinished`, {
    title: title.value,
  })
}

onMounted(async () => {
  nav.setLastWorkoutRoute('/workout-title')
  if (!telegramId) return
  try {
    const response = await axios.get(`${BASE_SITE}/workouts/users/${store.telegramId}/unfinished`)
    if (response.data?.title) {
      title.value = response.data.title
      store.setTitle(response.data.title)
    }
  } catch (e) {
    console.error('Ошибка при загрузке незавершённой тренировки', e)
  }
})

const goToExerciseSelect = () => {
    store.setTitle(title.value)
    router.push('/exercise-select')
}
</script>