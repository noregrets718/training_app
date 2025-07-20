<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">Тренировка от {{ formattedDate }}</h1>

    <div v-if="workout">
      <div
        v-for="exercise in workout.exercises"
        :key="exercise.id"
        class="mb-6"
      >
        <h2 class="text-lg font-semibold mb-2">Упражнение #{{ exercise.exercise.name }}</h2>
        <ul class="space-y-2">
          <li
            v-for="set in exercise.sets"
            :key="set.order"
            class="bg-white p-3 rounded-md border shadow-sm"
          >
            Подход {{ set.order }}: {{ set.weight }} кг × {{ set.repetitions }} раз
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, computed, inject } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { useNavigationStore } from '../stores/navigationStore'

const route = useRoute()
const nav = useNavigationStore()
const workoutId = route.params.id
console.log(workoutId)
const workout = ref<any>(null)
const BASE_SITE = inject("BASE_SITE");

onMounted(async () => {
  nav.setLastWorkoutRoute('/workout/:id')
  const res = await axios.get(`${BASE_SITE}/workouts/${workoutId}`,
    {
  headers: {
    'ngrok-skip-browser-warning': 'true'
  }
}
  )
  workout.value = res.data
  console.log(JSON.stringify(workout.value, null, 2))
  // console.log(workout.value)
})

const formattedDate = computed(() =>
  workout.value ? new Date(workout.value.day).toLocaleDateString() : ''
)
</script>