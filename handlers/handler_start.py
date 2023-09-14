from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.keyboard_main_menu import main_menu_keyboard

from time import sleep
# from bot_db.bot_database import cmd_start_db

router: Router = Router()


@router.message(Command('start'))
async def cmd_admin_start(message: Message):
    await message.answer(f'Hello, {message.from_user.username}!\n'
                         'Выбери пункт из меню:', reply_markup=main_menu_keyboard)
    # await cmd_start_db(message)
    await message.delete()
