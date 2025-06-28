import { createApp } from 'vue'
import './styles.css'
import App from './App.vue'
import router from './router'; 
import { createPinia } from 'pinia';

const pinia = createPinia();


const app =createApp(App).use(router).provide("BASE_SITE", "https://7285-80-64-17-22.ngrok-free.app")
app.use(pinia)
app.mount('#app');