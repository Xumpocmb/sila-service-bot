from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)
from bot_db.bot_db import DB


def make_prevention_back_kb():
    prevention_table = DB('sila_prevention.db').get_prevention('preventions')
    buttons = []
    buttons.append(InlineKeyboardButton(text='<< Назад к профилактикам', callback_data='preventions'))
    buttons = [[button] for button in buttons]
    prevention_back_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True,
                                       input_field_placeholder='Выберите действие..')
    return prevention_back_keyboard
