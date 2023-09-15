import sqlite3

from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery

from bot_db.bot_db import check_connection
from keyboards.gs.computer.keyboard_gs_computer import gs_computer_keyboard
from keyboards.gs.computer.keyboard_back_to_period import gs_keyboard

router: Router = Router()


@router.callback_query(F.data == 'gs-computer')
async def gs_computer(callback: CallbackQuery):
    await callback.message.answer(text='ГС для компьютерной техники.\nВыберите действие', reply_markup=gs_computer_keyboard)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(lambda data: F.data in ['gs-computer-24', 'gs-computer-premium-24', 'gs-computer-36', 'gs-computer-premium-36', 'gs-computer-repeat-24'])
async def gs_computer_other(callback: CallbackQuery):
    db, db_cursor = check_connection()
    if db and db_cursor:
        try:
            gs_id = callback.data
            result = db_cursor.execute(
                "SELECT gs_name, gs_description FROM gs-computer WHERE gs_id == '{key}'".format(key=gs_id)).fetchone()
            await callback.message.answer(
                text=f'<b>{result[0]}</b>\n'
                     f'<i>{result[1]}</i>',
                reply_markup=gs_keyboard)
        except sqlite3.Error as e:
            print("Ошибка SQLite:", e)
        finally:
            if db_cursor:
                db_cursor.close()
            if db:
                db.close()
            await callback.answer()

