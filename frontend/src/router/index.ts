import { createRouter, createWebHistory } from "vue-router";
// import Booking from "../views/DoctorDetail.vue";
import WorkoutList from "../views/WorkoutList.vue";
import CalendarPage from "../views/CalendarPage.vue";
import ExerciseSelect from "../views/ExerciseSelect.vue";
import SetsEntry from "../views/SetsEntry.vue";
import WorkoutDetail from "../views/WorkoutDetail.vue";
import StatsPage from "../views/StatsPage.vue";
import ProgramsPage from "../views/ProgramsPage.vue";
import AdminPanel from "../views/AdminPanel.vue";
import WorkoutTitle from "../views/WorkoutTitle.vue";

const routes = [
  { path: '/', name: "WorkoutList", component: WorkoutList },
  { path: '/calendar', component: CalendarPage },
  { path: '/exercise-select', component: ExerciseSelect },
  { path: '/sets-entry', component: SetsEntry },
  { path: '/workout/:id', component: WorkoutDetail},
  { path: '/stats', name: 'Stats', component: StatsPage },
  { path: '/programs', name: 'Programs', component: ProgramsPage },
  { path: '/admin', component: AdminPanel },
  { path: '/workout-title', component: WorkoutTitle },

//   { path: "/booking/:doctorId", name: "Booking", component: Booking },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    // Всегда прокручивать к верху страницы
    return { top: 0 };
  },
});

export default router;