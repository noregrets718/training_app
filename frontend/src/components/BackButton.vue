<template>
  <button
    @click="goBack"
    class="flex items-center gap-2 text-blue-600 hover:underline mb-4"
  >
    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none"
         viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M15 19l-7-7 7-7" />
    </svg>
    Назад
  </button>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

const goBack = () => {
  if (window.history.length > 1) {
    router.back()
  } else {
    router.push('/') // или другая fallback-страница
  }
}
</script>