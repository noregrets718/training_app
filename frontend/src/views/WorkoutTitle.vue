<template>
  <div class="p-6 max-w-md mx-auto bg-white rounded-lg shadow-md">
    <h1 class="text-2xl font-semibold mb-4 text-gray-900">Название тренировки</h1>

    <input
      v-model="title"
      placeholder="Например: Грудь/бицепс"
      class="w-full p-3 mb-4 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
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
import { ref } from 'vue'
import { useRouter} from 'vue-router'
import { useWorkoutStore } from '../stores/workoutStore'

const title = ref('')
const router = useRouter()
const store = useWorkoutStore()

const goToExerciseSelect = () => {
    store.setTitle(title.value)
    router.push('/exercise-select')
}
</script>