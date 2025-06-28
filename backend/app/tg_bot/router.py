from fastapi import APIRouter, Request, Depends
router = APIRouter()
from sqlalchemy.ext.asyncio import AsyncSession
from app.async_client import http_client_manager
from app.tg_bot.handlers import cmd_start, cmd_addexercise
from app.dao.session_maker_fast_api import db
from app.tg_bot.methods import bot_send_message
from app.config import settings


# @router.post("/webhook")
# async def webhook(request: Request, session: AsyncSession = Depends(db.get_db_with_commit)):
#     data = await request.json()
#     client = http_client_manager.get_client()

#     if "message" in data and "text" in data["message"]:
#         if data["message"]["text"] == "/start":
#             await cmd_start(client=client,
#                              session=session,
#                              user_info=data["message"]["from"])

    
#         elif data["message"]["text"] == "/addexercise":
#             await cmd_addexercise(client=client,
#                              session=session,
#                              user_info=data["message"]["from"])

#     return {"ok": True}
pending_add_exercise_users = set()

@router.post("/webhook")
async def webhook(request: Request, session: AsyncSession = Depends(db.get_db_with_commit)):
    data = await request.json()
    client = http_client_manager.get_client()
    message = data.get("message")
    
    if not message or "text" not in message:
        return {"ok": True}

    user_info = message["from"]
    text = message["text"].strip()
    telegram_id = user_info["id"]

    if text == "/start":
        await cmd_start(client=client, session=session, user_info=user_info)

    elif text == "/addexercise":
        if telegram_id not in settings.ADMIN_IDS:
            await bot_send_message(client, telegram_id, "❌ У вас нет прав для добавления упражнений.", None)
            return {"ok": True}

        pending_add_exercise_users.add(telegram_id)
        await bot_send_message(client, telegram_id, "Введите название упражнения:", None)

    elif telegram_id in pending_add_exercise_users:
        await cmd_addexercise(client=client, session=session, telegram_id=telegram_id, name=text)
        pending_add_exercise_users.remove(telegram_id)

    return {"ok": True}