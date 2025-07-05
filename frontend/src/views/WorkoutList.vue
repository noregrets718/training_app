<template>
  <div class="p-6 max-w-md mx-auto bg-white rounded-lg shadow-md">
    <h1 class="text-2xl font-semibold mb-6 text-gray-900">Мои тренировки</h1>

    <div v-if="loading" class="text-center text-gray-500 py-10">
      Загрузка...
    </div>

    <div v-else>
      <div v-if="workouts.length > 0">
        <ul class="space-y-3 mb-6">
          <li
            v-for="w in workouts"
            :key="w.id"
            @click="goToWorkout(w.id)"
            class="bg-gray-50 hover:bg-gray-100 cursor-pointer rounded-lg px-4 py-3 shadow-sm transition-shadow duration-200"
          >
            <span class="text-gray-900 font-medium">
              {{ new Date(w.day).toLocaleDateString() }}
            </span>
          </li>
        </ul>
      </div>

      <div v-else class="text-center text-gray-500 mb-6 italic">
        У вас ещё нет тренировок
      </div>

      <button
        @click="goAddWorkout"
        class="w-full bg-blue-600 hover:bg-blue-700 active:bg-blue-800 text-white font-medium rounded-lg shadow-md py-3 transition-colors duration-200"
        type="button"
      >
        ➕ Добавить тренировку
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, inject} from 'vue'
import { useRouter } from 'vue-router'
import { useWorkoutStore } from '../stores/workoutStore'
import axios from 'axios'

const store = useWorkoutStore()
const workouts = ref([])
const loading = ref(true)
const router = useRouter()

const telegramId = window.Telegram.WebApp.initDataUnsafe.user.id
store.setTelegramId(telegramId);
const BASE_SITE = inject("BASE_SITE");
console.log("Telegram ID:", telegramId);

onMounted(async () => {
  try {
    
   const res = await axios.get(`${BASE_SITE}/workouts/users/${telegramId}`, {
  headers: {
    'ngrok-skip-browser-warning': 'true'
  }
})
    console.log(res)
    workouts.value = res.data
    console.log(workouts.value)
    
  } catch (e) {
    workouts.value = [] // нет тренировок или ошибка
  } finally {
    loading.value = false
  }
})

const goAddWorkout = () => {
  router.push('/calendar')
}


const goToWorkout = (id) => {
  router.push(`/workout/${id}`)
}
</script>