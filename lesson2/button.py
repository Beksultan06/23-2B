from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram import types

MENU = ['Эспрессо', "Капучино", "Латте", "Американо", "3 в 1"]

keybord_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ИНФО")],
        [KeyboardButton(text="Контакты")],
        [KeyboardButton(text="О нас")],
        [KeyboardButton(text="Выбрать Напиток")],
    ],
    resize_keyboard=True
)

def generate_menu_keyboard():
    return types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text=menu)] for menu in MENU ],
        resize_keyboard=True
    )

def keyboard_confirm():
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='Да, потвердить')],
            [types.KeyboardButton(text='Отмена')],
        ],
        resize_keyboard=True
    )