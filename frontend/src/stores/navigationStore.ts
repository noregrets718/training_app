import { defineStore } from 'pinia'

export const useNavigationStore = defineStore('navigation', {
  state: () => ({
    lastWorkoutRoute: '/', // default подэкран "тренировок"
  }),
  actions: {
    setLastWorkoutRoute(route: string) {
      this.lastWorkoutRoute = route
    },
  },
})