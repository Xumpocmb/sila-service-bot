from bot_db.bot_db import DB
from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)


def make_gs_periods_kb(table_name):
    gs_tables = DB('sila.db').get_gs_periods(table=table_name)
    buttons = []
    for gs_id, gs_name in gs_tables:
        buttons.append(InlineKeyboardButton(text=gs_name, callback_data=gs_id))
    buttons = [[button] for button in buttons]
    gs_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True,
                                       input_field_placeholder='Выберите действие..')
    return gs_keyboard

