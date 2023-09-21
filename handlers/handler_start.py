from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.keyboard_main_menu import main_menu_keyboard

from time import sleep
# from bot_db.bot_database import cmd_start_db

router: Router = Router()


@router.message(Command('start'))
async def cmd_admin_start(message: Message):
    await message.answer(f'Доброго времени суток, мой юный падаван, {message.from_user.username}!\n'
                         f'Добро пожаловать в мир услуг Электросилы\n'
                         'Выбери нужный раздел и читай описание/наполнение каждой услуги', reply_markup=main_menu_keyboard)
    # await cmd_start_db(message)
    await message.delete()

