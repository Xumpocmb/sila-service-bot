from aiogram import Router
from aiogram.types import Message


from keyboards.keyboard_main_menu import main_menu_keyboard

router: Router = Router()


@router.message()
async def cmd_admin_echo(message: Message):
    await message.reply(text=LEXICON_RU['echo'], reply_markup=admin_main_menu_keyboard)


@router.message()
async def cmd_echo(message: Message):
    await message.reply(text=LEXICON_RU['echo'], reply_markup=main_menu_keyboard)
