from distutils.command.config import config
from tkinter.messagebox import YES
from tokenize import Token
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InputFile
from aiogram.utils import executor, exceptions
import requests
import sqlite3
import json

with open("config.json") as f:
    CONFIG = json.load(f)

TOKEN = CONFIG['TOKEN']
ADMIN_ID = CONFIG['ADMIN']


bot = Bot(token=TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# команда /start
@dp.message_handler(commands=['start'])
async def starts(message: types.Message):
    mark = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton("✅Да", callback_data="yes")
    no = types.InlineKeyboardButton("❌Нет", callback_data="no")
    mark.add(yes, no)
    await bot.send_message(ADMIN_ID,
     "Привет😇\nПеред тем как начать пользоваться ботом прочти политику проекта: *[клик](https://telegra.ph/Polzovatelskoe-sogloshenie-proekta-QiwiManager-05-29)*",
     reply_markup=mark)


@dp.callback_query_handler(lambda c: c.data)
async def callback_check(call: types.CallbackQuery):
    mes = call.data
    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, timeout=0)