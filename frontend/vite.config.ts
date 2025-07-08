import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [vue(), tailwindcss()],
  server: {
    host: '0.0.0.0', // Важно для Docker
    port: 5173,
    allowedHosts: [
      
      'localhost',
      '127.0.0.1',
      'https://7285-80-64-17-22.ngrok-free.app'
      // Можно добавить еще, если нужно
    ],
  },
})