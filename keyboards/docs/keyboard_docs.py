from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)


button_1: InlineKeyboardButton = InlineKeyboardButton(text='ГС', callback_data='doc-gs')
button_2: InlineKeyboardButton = InlineKeyboardButton(text='Профилактика', callback_data='doc-profilaktica')
button_3: InlineKeyboardButton = InlineKeyboardButton(text='Доп. Сервис', callback_data='doc-additional')
button_4: InlineKeyboardButton = InlineKeyboardButton(text='<< Назад', callback_data='main_menu')


choice_doc_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            button_1, button_2, button_3,
        ],
        [
            button_4,
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие..'
)