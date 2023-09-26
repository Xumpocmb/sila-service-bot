from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)
from bot_db.bot_db import DB


def make_category_menu_kb():
    insurances = DB('sila_itservice.db').get_all_tables()
    buttons = []
    for table_id, full_name in insurances:
        buttons.append(InlineKeyboardButton(text=full_name, callback_data=table_id))
    buttons.append(InlineKeyboardButton(text='<< Главное меню', callback_data='main_menu'))
    buttons = [[button] for button in buttons]
    itservice_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True,
                                       input_field_placeholder='Выберите действие..')
    return itservice_keyboard

