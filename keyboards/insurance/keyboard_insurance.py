from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)
from bot_db.bot_db import DB


def make_insurance_main_menu_kb():
    insurances = DB('sila_insurance.db').get_insurances()
    buttons = []
    for insurance_id, insurance_name in insurances:
        buttons.append(InlineKeyboardButton(text=insurance_name, callback_data=f'insurance-{insurance_id}'))
    buttons.append(InlineKeyboardButton(text='<< Главное меню', callback_data='main_menu'))
    buttons = [[button] for button in buttons]
    insurance_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True,
                                       input_field_placeholder='Выберите действие..')
    return insurance_keyboard

