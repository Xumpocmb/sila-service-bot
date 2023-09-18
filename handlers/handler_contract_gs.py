import sqlite3

from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.types.input_file import FSInputFile

router: Router = Router()


@router.callback_query(F.data == 'contract')
async def send_t_shirt(callback: CallbackQuery):
    document = FSInputFile('docs/GS.pdf')
    await callback.message.answer_document(document, caption='Договор оказания услуг Гарант Сервис')
    await callback.answer()
