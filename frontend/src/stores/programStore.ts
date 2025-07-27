// src/stores/program.ts
import { defineStore } from 'pinia'

export const useProgramStore = defineStore('program', {
  state: () => ({
    telegramId: null as number | null,
    title: '',
    description: '',
    weeks: [] as Week[],
  }),

  actions: {
    
    setTelegramId(id: number) {
      this.telegramId = id
    },

    setTitleDescription(title: string, description: string) {
      this.title = title
      this.description = description
    },

    addWeek() {
      this.weeks.push({
        title: `Неделя ${this.weeks.length + 1}`,
        days: [],
      })
    },

    addDay(weekIndex: number) {
      this.weeks[weekIndex].days.push({
        title: `День ${this.weeks[weekIndex].days.length + 1}`,
        exercises: [],
      })
    },

    addExercise(weekIndex: number, dayIndex: number, exerciseId: number, name: string) {
      this.weeks[weekIndex].days[dayIndex].exercises.push({
        exercise_id: exerciseId,
        name,
        sets: [],
      })
    },

    addSet(weekIndex: number, dayIndex: number, exerciseIndex: number, weight: number, repetitions: number) {
      this.weeks[weekIndex].days[dayIndex].exercises[exerciseIndex].sets.push({
        weight,
        repetitions,
      })
    },

    resetProgram() {
      this.title = ''
      this.description = ''
      this.weeks = []
    }
  }
})

// Типы:
interface Set {
  weight: number
  repetitions: number
}

interface Exercise {
  exercise_id: number
  name: string
  sets: Set[]
}

interface Day {
  title: string
  exercises: Exercise[]
}

interface Week {
  title: string
  days: Day[]
}
