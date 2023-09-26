import sqlite3

from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.types.input_file import FSInputFile

from keyboards.docs.keyboard_docs import choice_doc_keyboard
from keyboards.keyboard_main_menu import main_menu_keyboard

router: Router = Router()


@router.callback_query(F.data == 'docs')
async def docs(callback: CallbackQuery):
    await callback.message.answer(text='Выберите документ:', reply_markup=choice_doc_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'doc-gs')
async def send_doc_gs(callback: CallbackQuery):
    document = FSInputFile('docs/GS.pdf')
    await callback.message.answer_document(document, caption='Договор оказания услуг Гарант Сервис', reply_markup=main_menu_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'doc-profilaktica')
async def send_doc_profilaktica(callback: CallbackQuery):
    document = FSInputFile('docs/Profilaktika.pdf')
    await callback.message.answer_document(document, caption='Профилактика', reply_markup=main_menu_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'doc-additional')
async def send_doc_additional(callback: CallbackQuery):
    document = FSInputFile('docs/DopService.pdf')
    await callback.message.answer_document(document, caption='Доп Сервис', reply_markup=main_menu_keyboard)
    await callback.answer()
