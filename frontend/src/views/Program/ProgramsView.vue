<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">Программы</h1>
    <div class="flex space-x-4">
      <button @click="goTo('my')" class="btn">Мои программы</button>
      <button @click="goTo('shared')" class="btn">Программы пользователей</button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
const goTo = (type) => {
  router.push({ name: type === 'my' ? '/myprograms' : '/sharedprograms' })
}
</script>