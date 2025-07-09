 <template>
  <div class="p-4 max-w-2xl mx-auto">
    <h1 class="text-2xl font-bold mb-4">Упражнения</h1>

    <form @submit.prevent="addExercise" class="mb-4 flex gap-2">
      <input
        v-model="newExerciseName"
        placeholder="Новое упражнение"
        class="flex-1 border rounded px-3 py-2"
      />
      <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded">Добавить</button>
    </form>

    <ul class="space-y-2">
      <li v-for="exercise in exercises" :key="exercise.id" class="flex items-center gap-2">
        <input
          v-model="exercise.name"
          class="flex-1 border px-2 py-1 rounded"
        />
        <button @click="updateExercise(exercise)" class="text-green-600">💾</button>
        <button @click="deleteExercise(exercise.id)" class="text-red-600">🗑️</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue'
import axios from 'axios'

const BASE_SITE = inject("BASE_SITE")
const exercises = ref([])
const newExerciseName = ref('')

const fetchExercises = async () => {
  const res = await axios.get(`${BASE_SITE}/exercises`, {
    headers: { 'ngrok-skip-browser-warning': 'true' }
  })
  exercises.value = res.data
}

const addExercise = async () => {
  if (!newExerciseName.value.trim()) return
  await axios.post(`${BASE_SITE}/exercises`, { name: newExerciseName.value }, {
    headers: { 'ngrok-skip-browser-warning': 'true' }
  })
  newExerciseName.value = ''
  await fetchExercises()
}

const updateExercise = async (exercise) => {
  await axios.put(`${BASE_SITE}/exercises/${exercise.id}`, { name: exercise.name }, {
    headers: { 'ngrok-skip-browser-warning': 'true' }
  })
}

const deleteExercise = async (id) => {
  await axios.delete(`${BASE_SITE}/exercises/${id}`, {
    headers: { 'ngrok-skip-browser-warning': 'true' }
  })
  await fetchExercises()
}

onMounted(fetchExercises)
</script>