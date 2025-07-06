<script setup>
import { useRoute } from 'vue-router'
import BottomNavBar from './components/BottomNavBar.vue'

const route = useRoute()

const hiddenRoutes = ['/sets-entry', '/exercise-select']
</script>

<template>
  <div class="pb-20">
    <router-view />
    <BottomNavBar v-if="!hiddenRoutes.includes(route.path)" />
  </div>
</template>