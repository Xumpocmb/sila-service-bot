from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)


def make_back_to_periods_keyboard(table_name):
    button_1: InlineKeyboardButton = InlineKeyboardButton(text='<< Назад к срокам', callback_data=table_name)
    back_to_periods_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                button_1,
            ],
        ],
        resize_keyboard=True,
        input_field_placeholder='Выберите действие..'
    )

    return back_to_periods_keyboard
