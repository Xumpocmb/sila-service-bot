from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)

button_1: InlineKeyboardButton = InlineKeyboardButton(text='<< Назад к срокам', callback_data='gs-hoover')

gs_hoover_back_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            button_1,
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие..'
)
