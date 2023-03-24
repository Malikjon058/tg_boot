from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def gl_btn() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        KeyboardButton('Отправить фото 📸'),
        KeyboardButton('Отправить аудио 🎼')
    )

    return kb
