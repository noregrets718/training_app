from app.config import settings

main_kb = [
    [{"text": "📅 Мои записи", "callback_data": "booking"}],
    [{"text": "Тренировки", "web_app": {"url": f"{settings.FRONT_SITE}"}}],
    [{"text": "ℹ️ О нас", "callback_data": "about_us"}]
]