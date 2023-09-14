from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)


button_1: InlineKeyboardButton = InlineKeyboardButton(text='ГС', callback_data='gs')
button_2: InlineKeyboardButton = InlineKeyboardButton(text='Установка', callback_data='install')
button_3: InlineKeyboardButton = InlineKeyboardButton(text='Договор ГС', callback_data='contract')
button_4: InlineKeyboardButton = InlineKeyboardButton(text='IT-сервис', callback_data='service')
button_5: InlineKeyboardButton = InlineKeyboardButton(text='Страховка', callback_data='insurance')


main_menu_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            button_1, button_2, button_3
        ],
        [
            button_4, button_5,
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие..'
)
