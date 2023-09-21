from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery

from bot_db.bot_db import DB
from keyboards.prevention.keyboard_prevention import make_prevention_main_menu_kb
from keyboards.prevention.keyboard_prevention_back import make_prevention_back_kb

router: Router = Router()


@router.callback_query(F.data == 'preventions')
async def gs_type(callback: CallbackQuery):
    await callback.message.answer(text='Вы находитесь в меню ПРОФИЛАКТИКА.\nВыберите действие..',
                                  reply_markup=make_prevention_main_menu_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data.startswith('prevention_'))
async def gs_type_period_info(callback: CallbackQuery):
    description = DB('sila_prevention.db').get_prevention_desc(callback.data)
    await callback.message.answer(text=f'<i>{description[0]}</i>', reply_markup=make_prevention_back_kb())
    await callback.message.delete()
    await callback.answer()
