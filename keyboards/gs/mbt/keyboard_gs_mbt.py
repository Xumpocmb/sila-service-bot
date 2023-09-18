from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)

button_1: InlineKeyboardButton = InlineKeyboardButton(text='ГС 24 месяцев', callback_data='gs-mbt-premium-24')
button_2: InlineKeyboardButton = InlineKeyboardButton(text='ГС 36 месяцев', callback_data='gs-mbt-premium-36')
button_3: InlineKeyboardButton = InlineKeyboardButton(text='<< Назад в ГС', callback_data='gs')

gs_mbt_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            button_1,
        ], [
            button_2,
        ],
        [
            button_3,
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие..'
)
