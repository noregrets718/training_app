<template>
  <div class="p-6 max-w-md mx-auto bg-white rounded-lg shadow-md">
    <h1 class="text-2xl font-semibold mb-6 text-gray-900">Мои программы</h1>

    <div v-if="loading" class="text-center text-gray-500 py-10">
      Загрузка...
    </div>

    <div v-else>
      <div v-if="workouts.length > 0">
        <ul class="space-y-3 mb-6">
          <li
            v-for="w in programs"
            :key="w.id"
            class="bg-gray-50 hover:bg-gray-100 rounded-lg px-4 py-3 shadow-sm transition-shadow duration-200 flex justify-between items-center"
          >
            <div @click="goToProgram(w.id)" class="cursor-pointer flex-1">
              <span class="text-gray-900 font-medium">
                {{ new Date(w.day).toLocaleDateString() }} — {{ w.title }}
              </span>
            </div>
            <button
              @click.stop="deleteProgram(w.id)"
              class="ml-4 text-red-600 hover:text-red-800 text-sm"
            >
              ✖
            </button>
  </li> 
</ul>
      </div>

      <div v-else class="text-center text-gray-500 mb-6 italic">
        У вас ещё нет программ
      </div>

      <button
        @click="goAddProgram"
        class="w-full bg-blue-600 hover:bg-blue-700 active:bg-blue-800 text-white font-medium rounded-lg shadow-md py-3 transition-colors duration-200"
        type="button"
      >
        ➕ Составить программу
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, inject} from 'vue'
import { useRouter } from 'vue-router'
import { useProgramStore } from '../stores/programStore'
import axios from 'axios'

const store = useProgramStore()
const programs = ref([])
const loading = ref(true)
const router = useRouter()

const telegramId = window.Telegram.WebApp.initDataUnsafe.user.id
store.setTelegramId(telegramId);
const BASE_SITE = inject("BASE_SITE");
// console.log("Telegram ID:", telegramId);
// console.log("fddfdf");
// console.log(`${BASE_SITE}/workouts/users/${telegramId}`);
onMounted(async () => {
  try {
    
   const res = await axios.get(`${BASE_SITE}/programs/users/${telegramId}`, {
  headers: {
    'ngrok-skip-browser-warning': 'true'
  }
})
    // console.log(res)
    // console.log(BASE_SITE)
    // workouts.value = res.data
    // console.log(workouts.value)
    
  } catch (e) {
    programs.value = [] // нет тренировок или ошибка
  } finally {
    loading.value = false
  }
})

const goAddProgram = () => {
  router.push('/programs/create')
}


const goToProgram = (id) => {
  router.push(`/program/${id}`)
}

const deleteProgram = async (id) => {
  try {
    await axios.delete(`${BASE_SITE}/programs/${id}`, {
      headers: {
        'ngrok-skip-browser-warning': 'true'
      }
    });
    programs.value = programs.value.filter(w => w.id !== id); // удалить из списка
  } catch (e) {
    console.error('Ошибка при удалении программы', e);
    alert('Не удалось удалить программу');
  }
}
</script>