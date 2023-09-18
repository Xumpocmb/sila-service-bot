from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)
from bot_db.bot_db import DB


def make_gs_main_menu_kb():
    gs_tables = DB('sila_gs.db').get_all_gs_tables()
    buttons = []
    for gs_id, gs_full_name in gs_tables:
        buttons.append(InlineKeyboardButton(text=gs_full_name, callback_data=gs_id))
    buttons.append(InlineKeyboardButton(text='<< Главное меню', callback_data='main_menu'))
    buttons = [[button] for button in buttons]
    gs_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True,
                                       input_field_placeholder='Выберите действие..')
    return gs_keyboard

#
# button_1: InlineKeyboardButton = InlineKeyboardButton(text='ГС для мобильных устройств', callback_data='gs-mobile')
# button_2: InlineKeyboardButton = InlineKeyboardButton(text='ГС для компьютерной техники', callback_data='gs-computer')
# button_3: InlineKeyboardButton = InlineKeyboardButton(text='ГС для Стиральных/Сушильных/Посудомоечных машин',
#                                                       callback_data='gs-wash')
# button_4: InlineKeyboardButton = InlineKeyboardButton(text='ГС для АВ техники', callback_data='gs-av')
# button_5: InlineKeyboardButton = InlineKeyboardButton(text='ГС для Бытовой техники', callback_data='gs-appliances')
# button_6: InlineKeyboardButton = InlineKeyboardButton(text='ГС для для Кофеварок/Кофе машин',
#                                                       callback_data='gs-coffee-machine')
# button_7: InlineKeyboardButton = InlineKeyboardButton(text='ГС для для Вентиляторов', callback_data='gs-fan')
# button_8: InlineKeyboardButton = InlineKeyboardButton(text='ГС для для Холодильников', callback_data='gs-fridge')
# button_9: InlineKeyboardButton = InlineKeyboardButton(text='ГС для для Пылесосов', callback_data='gs-hoover')
# button_10: InlineKeyboardButton = InlineKeyboardButton(text='ГС для для мелкой бытовой техники', callback_data='gs-mbt')
# button_11: InlineKeyboardButton = InlineKeyboardButton(text='ГС для для мобильных кондиционеров',
#                                                        callback_data='gs-mobile-conditioner')
# button_12: InlineKeyboardButton = InlineKeyboardButton(text='ГС для для фото, цифровой тех.', callback_data='gs-photo')
# button_13: InlineKeyboardButton = InlineKeyboardButton(text='ГС для для электроинструмента',
#                                                        callback_data='gs-power-tool')
# button_14: InlineKeyboardButton = InlineKeyboardButton(text='ГС для для водонагревателей',
#                                                        callback_data='gs-water-heater')
# button_99: InlineKeyboardButton = InlineKeyboardButton(text='<< Главное меню', callback_data='main_menu')
#
# gs_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             button_1,
#         ],
#         [
#             button_2,
#         ],
#         [
#             button_3,
#         ],
#         [
#             button_4,
#         ],
#         [
#             button_5,
#         ],
#         [
#             button_6,
#         ],
#         [
#             button_7,
#         ],
#         [
#             button_8,
#         ],
#         [
#             button_9,
#         ],
#         [
#             button_10,
#         ],
#         [
#             button_11,
#         ],
#         [
#             button_12,
#         ],
#         [
#             button_13,
#         ],
#         [
#             button_14,
#         ],
#         [
#             button_99,
#         ],
#     ],
#     resize_keyboard=True,
#     input_field_placeholder='Выберите действие..'
# )
