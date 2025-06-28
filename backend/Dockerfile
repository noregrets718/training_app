FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем зависимости
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь backend-код
COPY . .

# Открываем порт
EXPOSE 8000


# Команда по умолчанию — запуск FastAPI-приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]