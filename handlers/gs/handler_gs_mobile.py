import sqlite3

from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards.gs.mobile.keyboard_gs_mobile import gs_mobile_keyboard
from keyboards.gs.mobile.keyboard_back_to_period import gs_keyboard

from bot_db.bot_db import check_connection

router: Router = Router()


@router.callback_query(F.data == 'gs-mobile')
async def gs_mobile(callback: CallbackQuery):
    await callback.message.answer(text='ГС для мобильных устройств.\nВыберите действие', reply_markup=gs_mobile_keyboard)
    await callback.answer()


@router.callback_query(lambda data: F.data in ['gs-mobile-12', 'gs-mobile-24', 'gs-mobile-repeat-12'])
@router.callback_query(lambda data: F.data in ['gs-mobile-12', 'gs-mobile-24', 'gs-mobile-repeat-12'])
@router.callback_query(lambda data: F.data in ['gs-mobile-12', 'gs-mobile-24', 'gs-mobile-repeat-12'])
async def gs_mobile_other(callback: CallbackQuery):
    db, db_cursor = check_connection()
    if db and db_cursor:
        try:
            gs_id = callback.data
            result = db_cursor.execute("SELECT gs_name, gs_description FROM gs_mobile WHERE gs_id == '{key}'".format(key=gs_id)).fetchone()
            await callback.message.answer(
                text=f'<b>{result[0]}</b>\n\n'
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
