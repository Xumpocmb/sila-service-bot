from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)

button_1: InlineKeyboardButton = InlineKeyboardButton(text='ГС 12 месяцев', callback_data='gs-mobile-conditioner-36')
button_4: InlineKeyboardButton = InlineKeyboardButton(text='<< Назад в ГС', callback_data='gs')

gs_mobile_conditioner_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            button_1,
        ], [
            button_4,
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие..'
)
