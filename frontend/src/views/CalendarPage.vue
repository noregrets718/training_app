<template>
  <div class="p-6 min-h-screen bg-gray-50 flex flex-col max-w-md mx-auto rounded-lg shadow-lg">
    <h1 class="text-xl font-bold mb-4 text-center">Выберите дату тренировки</h1>

    <div class="flex justify-between items-center mb-4">
      <button @click="prevMonth" class="text-2xl">⬅️</button>
      <div class="text-lg font-semibold">{{ currentMonth.format('MMMM YYYY') }}</div>
      <button @click="nextMonth" class="text-2xl">➡️</button>
    </div>

    <div class="grid grid-cols-7 gap-2 text-center text-sm">
      <div class="font-semibold text-gray-500" v-for="day in weekDays" :key="day">{{ day }}</div>

      <div
        v-for="n in firstDayOffset"
        :key="'empty-' + n"
        class="h-10"
      ></div>

      <div
        v-for="day in daysInMonth"
        :key="day.date"
        :class="[
          'h-12 rounded-md flex items-center justify-center text-sm transition border border-gray-200 cursor-default',
          isPast(day.date) ? 'text-gray-400 bg-gray-100 cursor-not-allowed' : ' hover:bg-blue-100',
          isToday(day.date) ? '' : '',
          selectedDate === day.date
            ? 'bg-blue-300 text-black font-semibold shadow-md border-blue-600'
            : 'text-gray-900'
        ]"
        @click="!isPast(day.date) && selectDate(day.date)"
      >
        {{ day.day }}
      </div>
    </div>

    <button
      @click="next"
      class="mt-6 w-full bg-blue-600 hover:bg-blue-700 active:bg-blue-800 text-white font-semibold rounded-lg shadow-md py-3 transition-colors duration-200"
      type="button"
    >
      Далее
    </button>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useWorkoutStore } from '../stores/workoutStore'
import { useRouter } from 'vue-router'
import dayjs from 'dayjs'
import 'dayjs/locale/ru'

dayjs.locale('ru')

const store = useWorkoutStore()
const router = useRouter()

const currentMonth = ref(dayjs().startOf('month'))
const selectedDate = ref('')

onMounted(() => {
  const today = dayjs()
  selectedDate.value = today.format('YYYY-MM-DD')
})

const weekDays = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

const daysInMonth = computed(() => {
  const start = currentMonth.value.startOf('month')
  const end = currentMonth.value.endOf('month')
  const days = []

  for (let date = start; date.isBefore(end) || date.isSame(end, 'day'); date = date.add(1, 'day')) {
    days.push({ date: date.format('YYYY-MM-DD'), day: date.date() })
  }

  return days
})

const firstDayOffset = computed(() => {
  const startWeekDay = currentMonth.value.startOf('month').day() || 7
  return startWeekDay - 1
})

const isToday = (date) => date === dayjs().format('YYYY-MM-DD')
const isPast = (date) => dayjs(date).isBefore(dayjs().startOf('day'))

const selectDate = (date) => {
  selectedDate.value = date
}

const prevMonth = () => {
  currentMonth.value = currentMonth.value.subtract(1, 'month')
}

const nextMonth = () => {
  currentMonth.value = currentMonth.value.add(1, 'month')
}

const next = () => {
  store.setDate(selectedDate.value)
  router.push('/workout-title')
}
</script>

<style scoped>
</style>
