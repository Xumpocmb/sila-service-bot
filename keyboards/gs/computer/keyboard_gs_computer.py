from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)

button_1: InlineKeyboardButton = InlineKeyboardButton(text='ГС 24 месяцев', callback_data='gs-computer-24')
button_2: InlineKeyboardButton = InlineKeyboardButton(text='ГС Премиум 24 месяцев', callback_data='gs-computer-premium-24')
button_3: InlineKeyboardButton = InlineKeyboardButton(text='ГС 36 месяцев', callback_data='gs-computer-36')
button_4: InlineKeyboardButton = InlineKeyboardButton(text='ГС Премиум 36 месяцев', callback_data='gs-computer-premium-36')
button_5: InlineKeyboardButton = InlineKeyboardButton(text='ГС повторный 24 месяцев', callback_data='gs-computer-repeat-24')
button_6: InlineKeyboardButton = InlineKeyboardButton(text='<< Назад в ГС', callback_data='gs')

gs_computer_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            button_1,
        ], [
            button_2,
        ], [
            button_3,
        ], [
            button_4,
        ], [
            button_5,
        ], [
            button_6,
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие..'
)
