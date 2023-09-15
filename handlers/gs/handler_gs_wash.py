import sqlite3

from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards.gs.wash.keyboard_gs_wash import gs_wash_keyboard
from keyboards.gs.wash.keyboard_back_to_period import gs_keyboard
from bot_db.bot_db import check_connection

router: Router = Router()


@router.callback_query(F.data == 'gs-wash')
async def gs_wash(callback: CallbackQuery):
    await callback.message.answer(text='ГС для мобильных устройств.\nВыберите действие', reply_markup=gs_wash_keyboard)
    await callback.answer()


@router.callback_query(lambda data: F.data in ['gs-wash-36', 'gs-wash-48', 'gs-wash-60'])
async def gs_wash_other(callback: CallbackQuery):
    db, db_cursor = check_connection()
    if db and db_cursor:
        try:
            gs_id = callback.data
            result = db_cursor.execute(
                "SELECT gs_name, gs_description FROM gs-wash WHERE gs_id == '{key}'".format(key=gs_id)).fetchone()
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
