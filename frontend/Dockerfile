# Стадия 1 — сборка проекта
FROM node:18-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build


# Стадия 2 — запуск с Nginx
FROM nginx:stable-alpine

# Удаляем дефолтную конфигурацию Nginx
RUN rm -rf /usr/share/nginx/html/*

# Копируем собранные файлы из стадии build
COPY --from=build /app/dist /usr/share/nginx/html

# Копируем свой nginx.conf (если есть)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 5173

CMD ["nginx", "-g", "daemon off;"]