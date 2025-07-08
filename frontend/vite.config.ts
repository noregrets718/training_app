import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [vue(), tailwindcss()],
  server: {
    host: '0.0.0.0',
    port: 5173,
    cors: true, // важно!
    strictPort: true,
    allowedHosts: ['trainingapp.ru'],
    hmr: {
      protocol: 'wss',
      host: 'trainingapp.ru',
      port: 5173,
      path: '/ws', // путь WebSocket (по умолчанию /, но можно указать явно)
    },
  },
})