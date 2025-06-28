from datetime import datetime
from httpx import AsyncClient
from loguru import logger
from app.config import settings


async def bot_send_message(client: AsyncClient, chat_id: int, text: str, kb: list[list[dict]] | None ):
    
    send_data = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    if kb:
        send_data["reply_markup"] = {"inline_keyboard": kb}
        logger.info("вызов bot_send_message")
    await client.post(f"{settings.get_tg_api_url()}/sendMessage", json=send_data)



def get_greeting_text():
    logger.info("вызов get_greeting_text")
    return "Добро пожаловать хуесос пролактиновый"