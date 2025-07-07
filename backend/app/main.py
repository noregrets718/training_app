import json
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
# from fastapi.staticfiles import StaticFiles
from app.workouts.router import router as workout_router
from app.exercises.router import router as exercise_router
from app.async_client import http_client_manager
from app.config import settings
from app.tg_bot.router import router as router_tg_bot


async def set_webhook(client):
    """Устанавливает вебхук для Telegram-бота."""
    try:
        response = await client.post(f"{settings.get_tg_api_url()}/setWebhook", json={
            "url": settings.get_webhook_url()
        })
        response_data = response.json()
        if response.status_code == 200 and response_data.get("ok"):
            logger.info(f"Webhook установлен: {response_data}")
        else:
            logger.error(f"Ошибка при установке вебхука: {response_data}")
    except Exception as e:
        logger.exception(f"Не удалось установить вебхук: {e}")

 


async def send_admin_msg(client, text): 
    for admin in settings.ADMIN_IDS:
        try:
            await client.post(f"{settings.get_tg_api_url()}/sendMessage",
                              json={"chat_id": admin, "text": text, "parse_mode": "HTML"})
        except Exception as E:
            logger.exception(f"Ошибка при отправке сообщения админу: {E}")



@asynccontextmanager 
async def lifespan(app: FastAPI):
    """Контекстный менеджер для настройки и завершения работы бота."""
    client = http_client_manager.get_client()
    logger.info("Настройка бота...")
    await set_webhook(client)
    await client.post(f"{settings.get_tg_api_url()}/setMyCommands",
                      data={"commands": json.dumps([{"command": "start", "description": "Главное меню"}])})
    await send_admin_msg(client, "Бот запущен!")
    yield
    logger.info("Завершение работы бота...")
    await send_admin_msg(client, "Бот остановлен!")
    await http_client_manager.close_client()
    

app = FastAPI(lifespan=lifespan)


# app.mount('/static', StaticFiles(directory='app/static'), name='static')


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:80",
        "http://localhost:5173",
        "https://2565-80-64-17-22.ngrok-free.app"  # ← сюда вставь свой ngrok-URL
    ],  # Разрешаем все источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы
    allow_headers=["*"],  # Разрешаем все заголовки
)

app.include_router(workout_router)
app.include_router(exercise_router)
app.include_router(router_tg_bot)