from email import message
from httpx import AsyncClient
from app.api.dao import UserDAO, ExerciseDAO
from app.api.schemas import TelegramIDModel, UserModel, ExerciseNameModel
from app.tg_bot.methods import get_greeting_text, bot_send_message
from app.tg_bot.kbs import main_kb
from app.config import settings
from sqlalchemy.exc import SQLAlchemyError







async def cmd_start(client: AsyncClient, session, user_info):
    user_in_db = await UserDAO.find_one_or_none(session=session, filters=TelegramIDModel(telegram_id=user_info["id"]))

    if not user_in_db:
        # Добавляем нового пользователя
        values = UserModel(
            telegram_id=user_info["id"],
            username=user_info.get("username"),
            
        )
        await UserDAO.add(session=session, values=values)

    message = get_greeting_text()
    await bot_send_message(client, user_info["id"], message, main_kb)




async def cmd_addexercise(client, session, telegram_id: int, name: str):
    exercise_in_db = await ExerciseDAO.find_one_or_none(
        session=session,
        filters=ExerciseNameModel(name=name)
    )
    if exercise_in_db:
        await bot_send_message(client, telegram_id, f"❗ Упражнение «{name}» уже существует.", None)
        return

    try:
        await ExerciseDAO.add(session=session, values=ExerciseNameModel(name=name))
        await bot_send_message(client, telegram_id, f"✅ Упражнение «{name}» добавлено.", None)
    except SQLAlchemyError:
        await session.rollback()
        await bot_send_message(client, telegram_id, "❌ Ошибка при добавлении упражнения.", None)

# async def cmd_addexercise(client: AsyncClient, session, user_info, message_text: str):
#     telegram_id = user_info["id"]

#     if telegram_id not in settings.ADMIN_IDS:
#         await bot_send_message(client, telegram_id, "⚠️ У вас нет прав для добавления упражнений.", None)
#         return

#     # Извлечь название упражнения из сообщения после команды, например: "/addexercise Приседания"
#     parts = message_text.strip().split(maxsplit=1)
#     if len(parts) < 2:
#         await bot_send_message(client, telegram_id, "❗ Пожалуйста, укажите название упражнения после команды.\nПример: /addexercise Приседания", None)
#         return
#     exercise_name = parts[1].strip()

#     # Проверяем, есть ли уже такое упражнение
#     exercise_in_db= await ExerciseDAO.find_one_or_none(session=session, filters=ExerciseNameModel(name=exercise_name))
#     if exercise_in_db:
#         await bot_send_message(client, telegram_id, f"❗ Упражнение «{exercise_name}» уже существует.", None)
#         return

#     # Добавляем новое упражнение
#     try:
#         new_exercise = await ExerciseDAO.add(session=session, name=exercise_name)
#         await session.commit()
#         await bot_send_message(client, telegram_id, f"✅ Упражнение «{exercise_name}» успешно добавлено.", None)
#     except SQLAlchemyError:
#         await session.rollback()
#         await bot_send_message(client, telegram_id, "❗ Ошибка при добавлении упражнения. Попробуйте ещё раз.", None)