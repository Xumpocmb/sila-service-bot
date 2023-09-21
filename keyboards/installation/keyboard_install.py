from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)
from bot_db.bot_db import DB


def make_install_main_menu_kb():
    gs_tables = DB('sila_installation.db').get_all_install_tables()
    buttons = []
    for gs_id, gs_full_name in gs_tables:
        buttons.append(InlineKeyboardButton(text=gs_full_name, callback_data=gs_id))
    buttons.append(InlineKeyboardButton(text='<< Главное меню', callback_data='main_menu'))
    buttons = [[button] for button in buttons]
    install_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True,
                                       input_field_placeholder='Выберите действие..')
    return install_keyboard

