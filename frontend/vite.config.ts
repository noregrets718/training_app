import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [vue(), tailwindcss()],
   server: {
    host: '0.0.0.0',
    port: 5173,
    allowedHosts: ['trainingapp.ru', 'www.trainingapp.ru'],
    hmr: {
      protocol: 'wss',  // или 'ws', если без SSL
      host: 'trainingapp.ru',
      port: 443, // если https, иначе 80 для http
      clientPort: 443, // порт, на котором клиент будет пытаться подключиться
    },
    
  },
})