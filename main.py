from aiogram import Bot, Dispatcher, types, executor
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import os

from database import MainDB
from keyboards import gl_btn

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '5627560688:AAHiup8He9yL_Dlv6AzDQCJ6Ch6a7WIQHJM'
ADMIN_GROUP_ID = -100671053760

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = MainDB()
db.create_table()


@dp.message_handler(commands=['Старт'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    db.add_user(user_id, username)

    btn = await gl_btn()
    await message.answer('Здравствуйте', reply_markup=btn)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)