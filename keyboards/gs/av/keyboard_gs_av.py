from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)

button_1: InlineKeyboardButton = InlineKeyboardButton(text='ГС Премиум Плюс на 12 мес', callback_data='gs-av-premium-plus-12')
button_2: InlineKeyboardButton = InlineKeyboardButton(text='ГС Повторный на 12 мес', callback_data='gs-av-repeat-12')
button_3: InlineKeyboardButton = InlineKeyboardButton(text='ГС Премиум на 36 мес', callback_data='gs-av-premium-plus-36')
button_4: InlineKeyboardButton = InlineKeyboardButton(text='ГС Премиум на 48 мес', callback_data='gs-av-premium-plus-48')
button_5: InlineKeyboardButton = InlineKeyboardButton(text='<< Назад в ГС', callback_data='gs')

gs_av_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
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
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие..'
)
