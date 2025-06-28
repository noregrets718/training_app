<template>
  <div class="p-6 max-w-md mx-auto bg-white rounded-lg shadow-md">
    <h1 class="text-2xl font-semibold mb-6 text-gray-900">Выберите упражнение</h1>

    <!-- Показываем уже добавленные упражнения -->
    <div v-if="store.exercises.length > 0" class="mb-6">
      <h2 class="text-lg font-medium mb-2 text-gray-800">Добавленные упражнения:</h2>
      <ul class="space-y-2">
        <li
          v-for="(ex, index) in store.exercises"
          :key="index"
          class="bg-gray-100 text-sm px-4 py-2 rounded"
        >
          {{ getExerciseName(ex.exercise_id) }} — {{ ex.sets.length }} подходов
        </li>
      </ul>
    </div>

    <!-- Выпадающий список упражнений -->
    <select
      v-model="exerciseId"
      class="w-full px-4 py-3 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-900"
    >
      <option disabled value="">Выберите упражнение</option>
      <option v-for="e in exercises" :key="e.id" :value="e.id">
        {{ e.name }}
      </option>
    </select>

    <!-- Кнопка Далее -->
    <button
      @click="next"
      :disabled="!exerciseId"
      class="w-full mt-6 bg-blue-600 hover:bg-blue-700 active:bg-blue-800 text-white font-medium rounded-lg shadow-md py-3 transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
    >
      Далее
    </button>

    <!-- Кнопка Завершить тренировку -->
    <button
      v-if="store.exercises.length > 0"
      @click="submit"
      class="w-full mt-4 bg-green-600 hover:bg-green-700 active:bg-green-800 text-white font-medium rounded-lg shadow-md py-3 transition-colors duration-200"
    >
      Завершить тренировку
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue'
import axios from 'axios'
import { useWorkoutStore } from '../stores/workoutStore'
import { useRouter } from 'vue-router'

const exerciseId = ref('')
const exercises = ref([])
const store = useWorkoutStore()
const router = useRouter()
const BASE_SITE = inject('BASE_SITE')

// Загрузка упражнений
onMounted(async () => {
  try {
    const res = await axios.get(`${BASE_SITE}/exercises`, {
      headers: { 'ngrok-skip-browser-warning': 'true' }
    })
    exercises.value = res.data
  } catch (error) {
    console.error('Ошибка при загрузке упражнений:', error)
  }
})

// Переход на страницу ввода подходов
const next = () => {
  store.setCurrentExerciseId(Number(exerciseId.value))
  router.push('/sets-entry')
}

// Завершение тренировки
const submit = async () => {
  try {
    await axios.post(`${BASE_SITE}/workouts`, {
      telegram_id: store.telegramId,
      workout_date: store.date,
      exercises: store.exercises
    }, {
      headers: { 'ngrok-skip-browser-warning': 'true' }
    })
    store.clearWorkout()
    router.push('/')
  } catch (err) {
    console.error('Ошибка при сохранении:', err)
    alert('Ошибка при сохранении тренировки')
  }
}

// Получение названия упражнения по ID
const getExerciseName = (id) => {
  const found = exercises.value.find(e => e.id === id)
  return found ? found.name : `ID ${id}`
}
</script>