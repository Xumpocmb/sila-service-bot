from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)

button_1: InlineKeyboardButton = InlineKeyboardButton(text='ГС 12 месяцев', callback_data='gs-power-tool-12')
button_2: InlineKeyboardButton = InlineKeyboardButton(text='ГС 24 месяцев', callback_data='gs-power-tool-24')
button_4: InlineKeyboardButton = InlineKeyboardButton(text='<< Назад в ГС', callback_data='gs')

gs_power_tool_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
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
