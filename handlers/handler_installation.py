from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery

from bot_db.bot_db import DB
from keyboards.installation.keyboard_back_to_period import make_back_to_periods_keyboard
from keyboards.installation.keyboard_install import make_install_main_menu_kb
from keyboards.installation.keyboard_periods import make_gs_periods_kb

router: Router = Router()


@router.callback_query(F.data == 'installations')
async def installation_type(callback: CallbackQuery):
    await callback.message.answer(text='Вы находитесь в меню Установки.\nВыберите действие..',
                                  reply_markup=make_install_main_menu_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data.startswith('install_'))
async def installation_type_periods(callback: CallbackQuery):
    await callback.message.answer(text='Выберите тип Установки', reply_markup=make_gs_periods_kb(callback.data))
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data.startswith('install-'))
async def installation_type_period_info(callback: CallbackQuery):
    table_name = f"{callback.data.split('-')[0]}_{callback.data.split('-')[1]}"
    db_info = DB('sila_installation.db').get_installation(install_id=callback.data, table=table_name)
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>',
                                  reply_markup=make_back_to_periods_keyboard(table_name))
    await callback.message.delete()
    await callback.answer()
