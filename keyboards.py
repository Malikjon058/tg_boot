from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

remove = ReplyKeyboardRemove()


async def gl_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row('Дать эффект фото')
    btn.row('Статистика', 'Связаться с админом!')
    return btn
