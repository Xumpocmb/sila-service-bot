from aiogram import Router
from aiogram.types import Message, CallbackQuery

from keyboards.keyboard_main_menu import main_menu_keyboard

router: Router = Router()


@router.message()
async def echo(message: Message):
    await message.reply(text='Используйте кнопки в меню!', reply_markup=main_menu_keyboard)


@router.callback_query()
async def gs_any_callback(callback: CallbackQuery):
    print(callback.data)
    await callback.message.reply('Не известная команда')
    await callback.answer()
