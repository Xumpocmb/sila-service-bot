from bot_db.bot_db import DB
from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)


def make_submenu_kb(table_name):
    install_tables = DB('sila_itservice.db').get_id_rows_from_table(table_name)
    buttons = []
    for table_id, table_name in install_tables:
        buttons.append(InlineKeyboardButton(text=table_name, callback_data=table_id))
    buttons.append(InlineKeyboardButton(text='<< Назад к меню IT-Сервис', callback_data='itservice'))
    buttons = [[button] for button in buttons]
    install = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True,
                                       input_field_placeholder='Выберите действие..')
    return install
