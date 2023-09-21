from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from bot_db.bot_db import DB
from keyboards.insurance.keyboard_insurance import make_insurance_main_menu_kb
from keyboards.insurance.keyboard_back_to_insurance import make_back_to_insurance

from states.states_insurances import MobilePriceState, YourselfPriceState, BikePriceState

router: Router = Router()


@router.callback_query(F.data == 'insurance')
async def insurance(callback: CallbackQuery):
    await callback.message.answer(text='Вы находитесь в меню Страховки.\nВыберите действие..',
                                  reply_markup=make_insurance_main_menu_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data.startswith('insurance-'))
async def get_insurance_description(callback: CallbackQuery):
    insurance_id = f"{callback.data.split('-')[1]}"
    db_info = DB('sila_insurance.db').get_insurance_description(insurance_id)
    await callback.message.answer(text=f'<i>{db_info[0]}</i>\n'
                                       f'<i>{db_info[1]}</i>\n'
                                       f'<i>{db_info[2]}</i>', reply_markup=make_back_to_insurance(insurance_id))
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'get-insurance-mobile')
async def ask_insurance_mobile(callback: CallbackQuery, state: FSMContext):
    await state.set_state(MobilePriceState.set_mobile_price)
    await callback.message.answer('Укажите стоимость телефона!')
    await callback.answer()


@router.message(MobilePriceState.set_mobile_price)
async def ask_insurance_mobile_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text.strip().replace(',', '.'))
    userdata = await state.get_data()
    await message.answer(f'Сумма страховки: {float(userdata["price"]) * 0.12}')
    await state.clear()


@router.callback_query(F.data == 'get-insurance-yourself')
async def ask_insurance_yourself(callback: CallbackQuery, state: FSMContext):
    await state.set_state(YourselfPriceState.set_mobile_price)
    await callback.message.answer('Укажите стоимость устройства!')
    await callback.answer()


@router.message(YourselfPriceState.set_mobile_price)
async def ask_insurance_yourself_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text.strip().replace(',', '.'))
    await state.set_state(YourselfPriceState.set_month_count)
    await message.answer('Укажите количество месяцев рассрочки!')


@router.message(YourselfPriceState.set_month_count)
async def ask_insurance_yourself_month(message: Message, state: FSMContext):
    await state.update_data(month=message.text.strip())
    userdata = await state.get_data()
    result = round((float(userdata['price']) * 0.00082) * float(userdata['month']), 2)
    await message.answer(f'Стоимость страховки: {result}')
    await state.clear()


@router.callback_query(F.data == 'get-insurance-bike')
async def ask_insurance_bike(callback: CallbackQuery, state: FSMContext):
    await state.set_state(BikePriceState.set_bike_price)
    await callback.message.answer('Укажите стоимость!')
    await callback.answer()


@router.message(BikePriceState.set_bike_price)
async def ask_insurance_bike_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text.strip())
    userdata = await state.get_data()
    result = round(float(userdata['price']) * 0.04, 2)
    await message.answer(f'Стоимость страховки: {result}')
    await state.clear()
