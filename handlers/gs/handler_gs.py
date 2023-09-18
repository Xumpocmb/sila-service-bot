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
from keyboards.gs.keyboard_back_to_period import make_back_to_periods_keyboard
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


@router.callback_query(F.data == 'gs')
async def gs_type(callback: CallbackQuery):
    await callback.message.answer(text='Вы находитесь в меню ГС.\nВыберите действие..', reply_markup=make_gs_main_menu_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data.startswith('gs_'))
async def gs_type_periods(callback: CallbackQuery):
    print(callback.data)
    await callback.message.answer(text='Выберите тип ГС', reply_markup=make_gs_periods_kb(callback.data))
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data.startswith('gs-'))
async def gs_type_period_info(callback: CallbackQuery):
    table_name = f"{callback.data.split('-')[0]}_{callback.data.split('-')[1]}"
    print(f'в таблице: {table_name} ищем: {callback.data}')
    db_info = DB('sila_gs.db').get_gs(gs_id=callback.data, table=table_name)
    await callback.message.answer(text=f'<b>{db_info[0]}</b>\n<i>{db_info[1]}</i>',
                                  reply_markup=make_back_to_periods_keyboard(table_name))
    await callback.message.delete()
    await callback.answer()


@router.callback_query()
async def gs_any_callback(callback: CallbackQuery):
    print(callback.data)
    await callback.message.reply('Не известная команда')
    await callback.answer()
