from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)

button_1: InlineKeyboardButton = InlineKeyboardButton(text='ГС для мобильных устройств', callback_data='gs-mobile')
button_2: InlineKeyboardButton = InlineKeyboardButton(text='ГС для компьютерной техники', callback_data='gs-computer')
button_3: InlineKeyboardButton = InlineKeyboardButton(text='ГС для Стиральных/Сушильных/Посудомоечных машин', callback_data='gs-wash')
button_4: InlineKeyboardButton = InlineKeyboardButton(text='ГС для АВ техники', callback_data='gs-av')
button_5: InlineKeyboardButton = InlineKeyboardButton(text='<< Главное меню', callback_data='main_menu')

gs_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            button_1,
        ],
        [
            button_2,
        ],
        [
            button_3,
        ],
        [
            button_4,
        ],
        [
            button_5,
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие..'
)
