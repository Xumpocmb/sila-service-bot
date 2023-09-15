import sqlite3

from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot_db.bot_db import check_connection
from keyboards.gs.appliances.keyboard_back_to_period import gs_appliances_back_keyboard
from keyboards.gs.appliances.keyboard_gs_appliances import gs_appliances_keyboard
from keyboards.gs.av.keyboard_back_to_period import gs_av_back_keyboard
from keyboards.gs.av.keyboard_gs_av import gs_av_keyboard
from keyboards.gs.coffee_machine.keyboard_back_to_period import gs_coffee_machine_back_keyboard
from keyboards.gs.coffee_machine.keyboard_gs_coffee_machine import gs_coffee_machine_keyboard
from keyboards.gs.computer.keyboard_back_to_period import gs_computer_back_keyboard
from keyboards.gs.computer.keyboard_gs_computer import gs_computer_keyboard
from keyboards.gs.keyboard_gs import gs_keyboard
from keyboards.gs.mobile.keyboard_back_to_period import gs_mobile_back_keyboard
from keyboards.gs.mobile.keyboard_gs_mobile import gs_mobile_keyboard
from keyboards.gs.wash.keyboard_back_to_period import gs_wash_back_keyboard
from keyboards.gs.wash.keyboard_gs_wash import gs_wash_keyboard

router: Router = Router()


def get_info_from_db(gs_id, table):
    db, db_cursor = check_connection()
    if db and db_cursor:
        try:
            result = db_cursor.execute(
                "SELECT gs_name, gs_description FROM {table_name} WHERE gs_id == '{key}'".format(key=gs_id, table_name=table)).fetchone()
            return result
        except sqlite3.Error as e:
            print("Ошибка SQLite:", e)
        finally:
            if db_cursor:
                db_cursor.close()
            if db:
                db.close()


def get_tables():
    conn = sqlite3.connect('sila.db')
    cursor = conn.cursor()
    tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    conn.close()
    return tables


def make_kb():
    table_list = get_tables()
    buttons = []

    for table in table_list:
        button_text = table[0]
        buttons.append(InlineKeyboardButton(text=button_text, callback_data=button_text))
    buttons = [[button] for button in buttons]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


@router.callback_query(F.data == 'gs')
async def send_t_shirt(callback: CallbackQuery):
    kb = make_kb()
    await callback.message.answer(text='Вы находитесь в меню ГС.\nВыберите действие..', reply_markup=kb)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'gs_appliances')
async def gs_appliances(callback: CallbackQuery):
    await callback.message.answer(text='ГС для Бытовой техники.\nВыберите действие', reply_markup=gs_appliances_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-appliances-36')
@router.callback_query(F.data == 'gs-appliances-48')
@router.callback_query(F.data == 'gs-appliances-60')
async def gs_appliances_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_appliances')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>', reply_markup=gs_appliances_back_keyboard)
    await callback.answer()

@router.callback_query(F.data == 'gs-mobile-12')
@router.callback_query(F.data == 'gs-mobile-24')
@router.callback_query(F.data == 'gs-mobile-repeat-12')
async def gs_mobile_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_mobile')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>', reply_markup=gs_mobile_back_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-wash')
async def gs_wash(callback: CallbackQuery):
    await callback.message.answer(text='ГС для стиральных, посудомоечных и сушильных машин.\nВыберите действие', reply_markup=gs_wash_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-wash-36')
@router.callback_query(F.data == 'gs-wash-48')
@router.callback_query(F.data == 'gs-wash-60')
async def gs_wash_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_wash')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>', reply_markup=gs_wash_back_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-coffee-machine')
async def gs_wash(callback: CallbackQuery):
    await callback.message.answer(text='ГС для для кофеварок/кофемашин.\nВыберите действие', reply_markup=gs_coffee_machine_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-coffee-machine-24')
@router.callback_query(F.data == 'gs-coffee-machine-36')
async def gs_wash_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_coffee_machine')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>', reply_markup=gs_coffee_machine_back_keyboard)
    await callback.answer()
