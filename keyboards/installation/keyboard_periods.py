from bot_db.bot_db import DB
from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)


def make_gs_periods_kb(table_name):
    gs_tables = DB('sila_installation.db').get_install_type(table=table_name)
    buttons = []
    for gs_id, gs_name in gs_tables:
        buttons.append(InlineKeyboardButton(text=gs_name, callback_data=gs_id))
    buttons.append(InlineKeyboardButton(text='<< Назад к Установкам', callback_data='installations'))
    buttons = [[button] for button in buttons]
    install = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True,
                                       input_field_placeholder='Выберите действие..')
    return install

