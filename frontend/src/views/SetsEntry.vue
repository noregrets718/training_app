<template>
  <div class="p-6 max-w-md mx-auto bg-white rounded-lg shadow-md">
    <h1 class="text-2xl font-semibold mb-6 text-gray-900">Подходы</h1>

    <ul class="mb-6 space-y-3">
      <li
        v-for="(set, index) in sets"
        :key="index"
        class="bg-gray-50 rounded-lg px-4 py-3 shadow-sm flex justify-between items-center"
      >
        <span class="text-gray-900 font-medium">
          Вес: {{ set.weight }} кг × Повторений: {{ set.repetitions }}
        </span>
        <button
          @click="removeSet(index)"
          class="text-red-500 hover:text-red-700 focus:outline-none"
          aria-label="Удалить подход"
        >
          ✕
        </button>
      </li>
    </ul>

    <button
      @click="showForm = true"
      class="w-full bg-blue-600 hover:bg-blue-700 active:bg-blue-800 text-white font-medium rounded-lg shadow-md py-3 transition-colors duration-200 mb-4"
      type="button"
    >
      ➕ Добавить подход
    </button>

    <div v-if="showForm" class="space-y-4 mb-6">
      <input
        v-model.number="weight"
        type="number"
        min="0"
        placeholder="Вес (кг)"
        class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      <input
        v-model.number="repetitions"
        type="number"
        min="1"
        placeholder="Количество повторений"
        class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      <button
        @click="addSet"
        class="w-full bg-green-600 hover:bg-green-700 active:bg-green-800 text-white font-medium rounded-lg shadow-md py-3 transition-colors duration-200"
        type="button"
      >
        Добавить
      </button>
      <button
        @click="cancel"
        class="w-full text-gray-600 hover:text-gray-800 underline mt-2"
        type="button"
      >
        Отмена
      </button>
    </div>

    <button
      v-if="sets.length > 0"
      @click="done"
      class="w-full bg-purple-600 hover:bg-purple-700 active:bg-purple-800 text-white font-medium rounded-lg shadow-md py-3 transition-colors duration-200"
      type="button"
    >
      Следующее упражнение
    </button>
     <button
      v-if="sets.length > 0"
      @click="submit"
      class="w-full bg-purple-600 hover:bg-purple-700 active:bg-purple-800 text-white font-medium rounded-lg shadow-md py-3 transition-colors duration-200 mt-4"
      type="button"
    >
      завершить тренировку
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useWorkoutStore } from '../stores/workoutStore'
import { useRouter } from 'vue-router'

const store = useWorkoutStore()
const router = useRouter()

const sets = ref([])
const weight = ref(null)
const repetitions = ref(null)
const showForm = ref(false)

const addSet = () => {
  if (weight.value > 0 && repetitions.value > 0) {
    sets.value.push({ weight: weight.value, repetitions: repetitions.value })
    weight.value = null
    repetitions.value = null
    showForm.value = false
  } else {
    alert('Введите корректные значения веса и повторений')
  }
}

const removeSet = (index) => {
  sets.value.splice(index, 1)
}

const cancel = () => {
  showForm.value = false
  weight.value = null
  repetitions.value = null
}

const done = () => {
  if (sets.value.length > 0 && store.currentExerciseId) {
    store.addExercise({ exercise_id: store.currentExerciseId, sets: [...sets.value] })
    sets.value = []
    store.setCurrentExerciseId(null)
    router.push('/exercise-select')
  } else {
    alert('Выберите упражнение и добавьте хотя бы один подход')
  }
}
const submit= () => {
  // Здесь можно сохранить данные в стор или отправить на сервер
  // Например: store.addSets(sets.value)
  router.push('/exercise-select')
}

</script>
