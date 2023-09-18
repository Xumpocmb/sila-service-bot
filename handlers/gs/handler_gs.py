import sqlite3

from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery

from bot_db.bot_db import DB
from keyboards.gs.appliances.keyboard_back_to_period import gs_appliances_back_keyboard
from keyboards.gs.appliances.keyboard_gs_appliances import gs_appliances_keyboard
from keyboards.gs.av.keyboard_back_to_period import gs_av_back_keyboard
from keyboards.gs.av.keyboard_gs_av import gs_av_keyboard
from keyboards.gs.coffee_machine.keyboard_back_to_period import gs_coffee_machine_back_keyboard
from keyboards.gs.coffee_machine.keyboard_gs_coffee_machine import gs_coffee_machine_keyboard
from keyboards.gs.computer.keyboard_back_to_period import gs_computer_back_keyboard
from keyboards.gs.computer.keyboard_gs_computer import gs_computer_keyboard
from keyboards.gs.fan.keyboard_back_to_period import gs_fan_back_keyboard
from keyboards.gs.fan.keyboard_gs_fan import gs_fan_keyboard
from keyboards.gs.fridge.keyboard_back_to_period import gs_fridge_back_keyboard
from keyboards.gs.fridge.keyboard_gs_fridge import gs_fridge_keyboard
from keyboards.gs.hoover.keyboard_back_to_period import gs_hoover_back_keyboard
from keyboards.gs.hoover.keyboard_gs_hoover import gs_hoover_keyboard
from keyboards.gs.keyboard_gs import make_gs_main_menu_kb
from keyboards.gs.keyboard_periods import make_gs_periods_kb
from keyboards.gs.mbt.keyboard_back_to_period import gs_mbt_back_keyboard
from keyboards.gs.mbt.keyboard_gs_mbt import gs_mbt_keyboard
from keyboards.gs.mobile.keyboard_back_to_period import gs_mobile_back_keyboard
from keyboards.gs.mobile.keyboard_gs_mobile import gs_mobile_keyboard
from keyboards.gs.mobile_conditioner.keyboard_back_to_period import gs_mobile_conditioner_back_keyboard
from keyboards.gs.mobile_conditioner.keyboard_gs_mobile_conditioner import gs_mobile_conditioner_keyboard
from keyboards.gs.photo.keyboard_back_to_period import gs_photo_back_keyboard
from keyboards.gs.photo.keyboard_gs_photo import gs_photo_keyboard
from keyboards.gs.power_tool.keyboard_back_to_period import gs_power_tool_back_keyboard
from keyboards.gs.power_tool.keyboard_gs_power_tool import gs_power_tool_keyboard
from keyboards.gs.wash.keyboard_back_to_period import gs_wash_back_keyboard
from keyboards.gs.wash.keyboard_gs_wash import gs_wash_keyboard
from keyboards.gs.water_heater.keyboard_back_to_period import gs_water_heater_back_keyboard
from keyboards.gs.water_heater.keyboard_gs_water_heater import gs_water_heater_keyboard

router: Router = Router()


def get_info_from_db(gs_id, table):
    db, db_cursor = DB('sila.db').check_connection()
    if db and db_cursor:
        try:
            result = db_cursor.execute(
                "SELECT gs_name, gs_description FROM {table_name} WHERE gs_id == '{key}'".format(key=gs_id,
                                                                                                 table_name=table)).fetchone()
            return result
        except sqlite3.Error as e:
            print("Ошибка SQLite:", e)
        finally:
            if db_cursor:
                db_cursor.close()
            if db:
                db.close()


@router.callback_query(F.data == 'gs')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text='Вы находитесь в меню ГС.\nВыберите действие..', reply_markup=make_gs_main_menu_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'gs_av')
async def gs_av(callback: CallbackQuery):
    await callback.message.answer(text='ГС для Аудио-Видео техники.\nВыберите действие', reply_markup=make_gs_periods_kb(callback.data))
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'gs-av-premium-plus-12')
@router.callback_query(F.data == 'gs-av-repeat-12')
@router.callback_query(F.data == 'gs-av-premium-plus-36')
@router.callback_query(F.data == 'gs-av-premium-plus-48')
async def gs_av_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_av')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>', reply_markup=gs_av_back_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-appliances')
async def gs_appliances(callback: CallbackQuery):
    await callback.message.answer(text='ГС для Бытовой техники.\nВыберите действие',
                                  reply_markup=gs_appliances_keyboard)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'gs-appliances-36')
@router.callback_query(F.data == 'gs-appliances-48')
@router.callback_query(F.data == 'gs-appliances-60')
async def gs_appliances_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_appliances')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>',
                                  reply_markup=gs_appliances_back_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-mobile')
async def gs_mobile(callback: CallbackQuery):
    await callback.message.answer(text='ГС для мобильных устройств.\nВыберите действие',
                                  reply_markup=gs_mobile_keyboard)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'gs-mobile-12')
@router.callback_query(F.data == 'gs-mobile-24')
@router.callback_query(F.data == 'gs-mobile-repeat-12')
async def gs_mobile_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_mobile')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>',
                                  reply_markup=gs_mobile_back_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-wash')
async def gs_wash(callback: CallbackQuery):
    await callback.message.answer(text='ГС для стиральных, посудомоечных и сушильных машин.\nВыберите действие',
                                  reply_markup=gs_wash_keyboard)
    await callback.message.delete()
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
    await callback.message.answer(text='ГС для для кофеварок/кофемашин.\nВыберите действие',
                                  reply_markup=gs_coffee_machine_keyboard)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'gs-coffee-machine-24')
@router.callback_query(F.data == 'gs-coffee-machine-36')
async def gs_wash_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_coffee_machine')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>',
                                  reply_markup=gs_coffee_machine_back_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-computer')
async def gs_computer(callback: CallbackQuery):
    await callback.message.answer(text='ГС для компьютерной техники.\nВыберите действие',
                                  reply_markup=gs_computer_keyboard)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'gs-computer-24')
@router.callback_query(F.data == 'gs-computer-premium-24')
@router.callback_query(F.data == 'gs-computer-36')
@router.callback_query(F.data == 'gs-computer-premium-36')
@router.callback_query(F.data == 'gs-computer-repeat-24')
async def gs_computer_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_computer')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>',
                                  reply_markup=gs_computer_back_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-coffee-machine')
async def gs_coffee(callback: CallbackQuery):
    await callback.message.answer(text='ГС для кофеварок/кофемашин.\nВыберите действие',
                                  reply_markup=gs_coffee_machine_keyboard)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'gs-coffee-machine-24')
@router.callback_query(F.data == 'gs-coffee-machine-36')
async def gs_coffee_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_coffee_machine')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>',
                                  reply_markup=gs_coffee_machine_back_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-fan')
async def gs_fan(callback: CallbackQuery):
    await callback.message.answer(text='ГС для для вентиляторов.\nВыберите действие', reply_markup=gs_fan_keyboard)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'gs-fan-36')
async def gs_fan_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_fan')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>', reply_markup=gs_fan_back_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-fridge')
async def gs_fridge(callback: CallbackQuery):
    await callback.message.answer(text='ГС для для холодильников/морозильников.\nВыберите действие',
                                  reply_markup=gs_fridge_keyboard)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'gs-fridge-48')
@router.callback_query(F.data == 'gs-fridge-60')
async def gs_fridge_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_fridge')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>',
                                  reply_markup=gs_fridge_back_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-hoover')
async def gs_hoover(callback: CallbackQuery):
    await callback.message.answer(text='ГС для для пылесосов.\nВыберите действие', reply_markup=gs_hoover_keyboard)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'gs-hoover-36')
async def gs_hoover_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_hoover')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>',
                                  reply_markup=gs_hoover_back_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-mbt')
async def gs_mbt(callback: CallbackQuery):
    await callback.message.answer(text='ГС для для мелкой бытовой техники.\nВыберите действие',
                                  reply_markup=gs_mbt_keyboard)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'gs-mbt-premium-24')
@router.callback_query(F.data == 'gs-mbt-premium-36')
async def gs_mbt_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_mbt')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>', reply_markup=gs_mbt_back_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-mobile-conditioner')
async def gs_mobile_conditioner(callback: CallbackQuery):
    await callback.message.answer(text='ГС для для мобильных кондиционеров.\nВыберите действие',
                                  reply_markup=gs_mobile_conditioner_keyboard)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'gs-mobile-conditioner-36')
async def gs_mobile_conditioner_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_mobile_conditioner')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>',
                                  reply_markup=gs_mobile_conditioner_back_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-photo')
async def gs_photo(callback: CallbackQuery):
    await callback.message.answer(text='ГС для для фото, цифровой тех.\nВыберите действие',
                                  reply_markup=gs_photo_keyboard)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'gs-photo-36')
@router.callback_query(F.data == 'gs-photo-24')
async def gs_photo_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_photo')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>', reply_markup=gs_photo_back_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-power-tool')
async def gs_power_tool(callback: CallbackQuery):
    await callback.message.answer(text='ГС для для электроинструмента.\nВыберите действие',
                                  reply_markup=gs_power_tool_keyboard)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'gs-power-tool-12')
@router.callback_query(F.data == 'gs-power-tool-24')
async def gs_power_tool_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_power_tool')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>',
                                  reply_markup=gs_power_tool_back_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-water-heater')
async def gs_power_tool(callback: CallbackQuery):
    await callback.message.answer(text='ГС для для водонагревателей.\nВыберите действие',
                                  reply_markup=gs_water_heater_keyboard)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'gs-water-heater-24')
@router.callback_query(F.data == 'gs-water-heater-36')
async def gs_power_tool_other(callback: CallbackQuery):
    db_info = get_info_from_db(gs_id=callback.data, table='gs_water_heater')
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>',
                                  reply_markup=gs_water_heater_back_keyboard)
    await callback.answer()


@router.callback_query()
async def gs_any_callback(callback: CallbackQuery):
    await callback.message.answer(text=callback.data,
                                  reply_markup=gs_water_heater_keyboard)
    await callback.message.delete()
    await callback.answer()
