from distutils.command.config import config
from re import A
from tkinter import Button
from tkinter.messagebox import YES
from tokenize import Token
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InputFile
from aiogram.utils import executor, exceptions
import keyb as k

from sqlhandl import SqlH
import json

with open("config.json") as f:
    CONFIG = json.load(f)

TOKEN = CONFIG['TOKEN']
ADMIN_ID = CONFIG['ADMIN']

# BOT CONNECTING
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# команда /start (command /start)
@dp.message_handler(commands=['start'])
async def starts(message: types.Message):
    await bot.send_message(ADMIN_ID,
     "Привет😇\nПеред тем как начать пользоваться ботом прочти политику проекта: *[клик](https://telegra.ph/Polzovatelskoe-sogloshenie-proekta-QiwiManager-05-29)*",
     reply_markup=k.mark)


# команда /menu (command /menu)
@dp.message_handler(commands=['menu'])
async def menu(message: types.Message):
    await bot.send_photo(message.from_user.id, photo="https://imgur.com/a/WEi7QF4", caption="Добро пожаловать", reply_markup=k.main)

# Test Generator Inline Keyboard
@dp.message_handler(commands=['test'])
async def test(message: types.Message):
    list_button_name = ['api', 'apo', 'test']

    button_list = []
    for item in list_button_name:
        button_list.append([types.InlineKeyboardButton(text=item, callback_data=item)])

    test = types.InlineKeyboardMarkup(inline_keyboard=button_list)
    await bot.send_message(message.from_user.id, "TEST", reply_markup=test)


# Обработчик текста (Text handler)
@dp.message_handler(content_types=types.ContentTypes.ANY)
async def all(message: types.Message):
    mes = message.text

    if mes == "API токены💻":
        pass
        


# Обработчик callback'ов (callback handler)
@dp.callback_query_handler(lambda c: c.data)
async def callback_check(call: types.CallbackQuery):
    mes = call.data

    if mes == "yes":
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, photo="https://imgur.com/a/WEi7QF4", caption="Добро пожаловать", reply_markup=k.main)
    


# Exploiting
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, timeout=0)