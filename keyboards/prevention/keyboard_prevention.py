from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)
from bot_db.bot_db import DB


def make_prevention_main_menu_kb():
    prevention_table = DB('sila_prevention.db').get_prevention('preventions')
    buttons = []
    for prevention_id, prevention_name in prevention_table:
        buttons.append(InlineKeyboardButton(text=prevention_name, callback_data=prevention_id))
    buttons.append(InlineKeyboardButton(text='<< Главное меню', callback_data='main_menu'))
    buttons = [[button] for button in buttons]
    prevention_main_menu_kb = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True,
                                       input_field_placeholder='Выберите действие..')
    return prevention_main_menu_kb

