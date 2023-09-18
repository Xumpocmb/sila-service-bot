from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards.keyboard_admin_panel import admin_panel_keyboard

router: Router = Router()


@router.callback_query(F.data == 'admin_panel')
async def gs_type(callback: CallbackQuery):
    await callback.message.answer(text='ПАНЕЛЬ УПРАВЛЕНИЯ.\nВыберите действие..',
                                  reply_markup=admin_panel_keyboard)
    await callback.message.delete()
    await callback.answer()
