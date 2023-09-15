import sqlite3

from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards.gs.av.keyboard_gs_av import gs_av_keyboard
from keyboards.gs.av.keyboard_back_to_period import gs_keyboard

from bot_db.bot_db import check_connection

router: Router = Router()


@router.callback_query(F.data == 'gs-av')
async def gs_av(callback: CallbackQuery):
    await callback.message.answer(text='ГС для Аудио-Видео техники.\nВыберите действие', reply_markup=gs_av_keyboard)
    await callback.answer()


@router.callback_query(lambda data: F.data in ['gs-av-premium-plus-12', 'gs-av-repeat-12', 'gs-av-premium-plus-36', 'gs-av-premium-plus-48'])
async def gs_av_premium_plus_12(callback: CallbackQuery):
    db, db_cursor = check_connection()
    if db and db_cursor:
        try:
            gs_id = callback.data
            result = db_cursor.execute("SELECT gs_name, gs_description FROM gs_av WHERE gs_id == '{key}'".format(key=gs_id)).fetchone()
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


# @router.callback_query(F.data == 'gs-av-repeat-12')
# async def gs_av_repeat_12(callback: CallbackQuery):
#     db, db_cursor = check_connection()
#     if db and db_cursor:
#         try:
#             gs_id = callback.data
#             result = db_cursor.execute(
#                 "SELECT gs_name, gs_description FROM gs_av WHERE gs_id == '{key}'".format(key=gs_id)).fetchone()
#             await callback.message.answer(
#                 text=f'<b>{result[0]}</b>\n'
#                      f'<i>{result[1]}</i>',
#                 reply_markup=gs_keyboard)
#         except sqlite3.Error as e:
#             print("Ошибка SQLite:", e)
#         finally:
#             if db_cursor:
#                 db_cursor.close()
#             if db:
#                 db.close()
#             await callback.answer()
#
#
# @router.callback_query(F.data == 'gs-av-premium-plus-36')
# async def gs_av_premium_plus_36(callback: CallbackQuery):
#     await callback.message.answer(text="""
#     <b>3</b>\n
#     """, reply_markup=gs_keyboard)
#     await callback.answer()
#
#
# @router.callback_query(F.data == 'gs-av-premium-plus-48')
# async def send_t_shirt(callback: CallbackQuery):
#     await callback.message.answer(text="""
#     <b>4</b>\n
#     """, reply_markup=gs_keyboard)
#     await callback.answer()
