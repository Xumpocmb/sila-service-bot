from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)


def make_back_to_insurance(insurance_id):
    button_1: InlineKeyboardButton = InlineKeyboardButton(text='Рассчитать стоимость страховки', callback_data=f'get-insurance-{insurance_id}')
    button_2: InlineKeyboardButton = InlineKeyboardButton(text='<< Назад к страховкам', callback_data='insurance')
    back_to_insurance_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                button_1,
            ],
            [
                button_2,
            ],
        ],
        resize_keyboard=True,
        input_field_placeholder='Выберите действие..'
    )

    return back_to_insurance_keyboard
