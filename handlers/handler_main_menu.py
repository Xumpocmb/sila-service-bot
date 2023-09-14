from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards.keyboard_main_menu import main_menu_keyboard

router: Router = Router()


@router.callback_query(F.data == 'main_menu')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text='Главное меню.\nВыберите действие', reply_markup=main_menu_keyboard)
    await callback.message.delete()
    await callback.answer()
