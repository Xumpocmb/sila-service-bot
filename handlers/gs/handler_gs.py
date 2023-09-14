from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards.gs.keyboard_gs import gs_keyboard


router: Router = Router()


@router.callback_query(F.data == 'gs')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text='Вы находитесь в меню ГС.\nВыберите действие..', reply_markup=gs_keyboard)
    await callback.message.delete()
    await callback.answer()
