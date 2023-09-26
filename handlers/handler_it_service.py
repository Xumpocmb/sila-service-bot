from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery

from bot_db.bot_db import DB
from keyboards.itservice.keyboard_back_to_submenu import make_back_to_submenu_keyboard
from keyboards.itservice.keyboard_itservice import make_category_menu_kb
from keyboards.itservice.keyboard_sub_menu import make_submenu_kb

router: Router = Router()


@router.callback_query(F.data == 'itservice')
async def it_service_menu(callback: CallbackQuery):
    await callback.message.answer(text='Вы находитесь в меню IT-Сервис.\nВыберите действие..',
                                  reply_markup=make_category_menu_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data.startswith('itservice_'))
async def it_service_sub_menu(callback: CallbackQuery):
    table_name = callback.data
    await callback.message.answer(text='Выберите тип', reply_markup=make_submenu_kb(callback.data))
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data.startswith('itservice-'))
async def it_service_description(callback: CallbackQuery):
    table_name = f"{callback.data.split('-')[0]}_{callback.data.split('-')[1]}"
    db_info = DB('sila_itservice.db').get_description(itservice_id=callback.data, table=table_name)
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>', reply_markup=make_back_to_submenu_keyboard(table_name))
    await callback.message.delete()
    await callback.answer()
