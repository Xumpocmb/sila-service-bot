from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)

button_1: InlineKeyboardButton = InlineKeyboardButton(text='ГС 36 месяцев', callback_data='gs-appliances-36')
button_2: InlineKeyboardButton = InlineKeyboardButton(text='ГС 48 месяцев', callback_data='gs-appliances-48')
button_3: InlineKeyboardButton = InlineKeyboardButton(text='ГС 60 месяцев', callback_data='gs-appliances-60')
button_4: InlineKeyboardButton = InlineKeyboardButton(text='<< Назад в ГС', callback_data='gs')

gs_appliances_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            button_1,
        ], [
            button_2,
        ], [
            button_3,
        ], [
            button_4,
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие..'
)
