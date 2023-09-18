from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)


button_1: InlineKeyboardButton = InlineKeyboardButton(text='Добавить ГС', callback_data='add-gs')
button_2: InlineKeyboardButton = InlineKeyboardButton(text='Удалить ГС', callback_data='del-gs')
button_6: InlineKeyboardButton = InlineKeyboardButton(text='Главное меню', callback_data='main_menu')


admin_panel_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            button_1, button_2,
        ],
        [
            button_6,
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие..'
)
