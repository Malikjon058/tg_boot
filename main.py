import logging

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InputFile
from aiogram.utils.executor import start_polling
from database import *
from keyboards import gl_btn

logging.basicConfig(level=logging.INFO)


storage = MemoryStorage()
BOT_TOKEN = "5627560688:AAHiup8He9yL_Dlv6AzDQCJ6Ch6a7WIQHJM"
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
db = MainDB()
db.create_table()


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    btn = await gl_btn()
    await message.answer('Здравствуйте', reply_markup=btn)



@dp.message_handler(content_types=[types.ContentType.PHOTO])
async def process_photo(message: types.Message):
    photo = message.photo[-1].file_id
    user = message.from_user.id
    db.insert_photo(photo=photo, user=user)
    await message.answer('Фото сохранено')


@dp.message_handler(content_types=[types.ContentType.AUDIO])
async def process_audio(message: types.Message):
    audio = message.audio.file_id
    user = message.from_user.id
    db.insert_audio(user=user, audio=audio)
    await message.answer('Аудио сохранено')

@dp.message_handler(commands=['файлы'])
async def get_files(message: types.Message):
    user = message.from_user.id
    db.select_data(user)
    for file_id, file_type in db.select_data():
        if file_type == 'photo':
            await message.answer_photo(InputFile(file_id))
        elif file_type == 'audio':
            await message.answer_audio(InputFile(file_id))

if __name__ == '__main__':
    start_polling(dp, skip_updates=True)

