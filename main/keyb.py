# клавиатуры keyboards
from aiogram import types

# Основное меню (main menu)
main = types.ReplyKeyboardMarkup(resize_keyboard=True) # Основная клавиатура
tokens = types.KeyboardButton("API токены💻") # Токены
control_panel = types.KeyboardButton("Управление🛠") # Управление тоткенами
settings_panel = types.KeyboardButton("Настрйоки⚙") # Настройки
back_to_menu = types.KeyboardButton("⬅Назад")
main.add(tokens, control_panel)

# Согласие на политику тип
mark = types.InlineKeyboardMarkup() # Inline клавиатура
yes = types.InlineKeyboardButton("✅Да", callback_data="yes") # да
no = types.InlineKeyboardButton("❌Нет", callback_data="no") # нет

# Добавить токены
keyboard = types.InlineKeyboardMarkup(row_width=2)
add_token = types.InlineKeyboardButton("Добавить token", callback_data="add_token") # Callback инлайна
add_tokens_from_file = types.InlineKeyboardButton("Добавить тоткены из файла", callback_data="add_tokens_from_file") # Добавления токенов из файлов
keyboard.add(add_token, add_tokens_from_file)