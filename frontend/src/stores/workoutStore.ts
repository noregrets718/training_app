import { defineStore } from 'pinia'

export const useWorkoutStore = defineStore('workout', {
  state: () => ({
    telegramId: null as number | null,
    date: '', // выбранная дата тренировки, строка 'YYYY-MM-DD'
    currentExerciseId: null as number | null, // выбранное упражнение на текущем шаге
    exercises: [] as {
      exercise_id: number
      sets: { weight: number; repetitions: number }[]
    }[]
  }),
  actions: {

    setTelegramId(id: number) {
      this.telegramId = id
    },

    setDate(date: string) {
      this.date = date
    },
    setCurrentExerciseId(id: number) {
      this.currentExerciseId = id
    },
    addSetToCurrentExercise(set: { weight: number; repetitions: number }) {
      if (this.currentExerciseId === null) return

      const exercise = this.exercises.find(e => e.exercise_id === this.currentExerciseId)
      if (exercise) {
        exercise.sets.push(set)
      } else {
        // Если упражнения нет — создаем с одним подходом
        this.exercises.push({
          exercise_id: this.currentExerciseId,
          sets: [set]
        })
      }
    },


    addExercise(exercise:{ exercise_id:number; sets:[]}) {
       this.exercises.push(exercise)
  },



    clearWorkout() {
      this.date = ''
      this.currentExerciseId = null
      this.exercises = []
    }
  }
})