from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)

button_1: InlineKeyboardButton = InlineKeyboardButton(text='ГС 36 месяцев', callback_data='gs-photo-36')
button_2: InlineKeyboardButton = InlineKeyboardButton(text='ГС 24 месяцев', callback_data='gs-photo-24')
button_4: InlineKeyboardButton = InlineKeyboardButton(text='<< Назад в ГС', callback_data='gs')

gs_photo_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            button_1,
        ],
        [
            button_2,
        ],
        [
            button_4,
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие..'
)
