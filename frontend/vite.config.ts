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
    allowedHosts: ['trainingapp.ru, www.trainingapp.ru'],
    hmr: {
      protocol: 'wss',
      host: 'trainingapp.ru',
      clientPort: 443
      // path: '/ws', // путь WebSocket (по умолчанию /, но можно указать явно)     // это то, что слушает Vite внутри
    },
  },
})