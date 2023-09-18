from aiogram import F
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import Message


from keyboards.keyboard_admin_panel import admin_panel_keyboard
from keyboards.keyboard_cancel import cancel_keyboard

from states.StatesGS import AddGSState

router: Router = Router()


@router.callback_query(F.data == 'admin_panel')
async def send_admin_panel(callback: CallbackQuery):
    await callback.message.answer(text='ПАНЕЛЬ УПРАВЛЕНИЯ.\nВыберите действие..',
                                  reply_markup=admin_panel_keyboard)
    await callback.message.delete()
    await callback.answer()


@router.message(F.text == 'Отмена')
async def choosing_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.reply('Создание товара отменено!', reply_markup=admin_panel_keyboard)


@router.callback_query(F.data == 'add-gs')
async def add_gs_callback(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AddGSState.GS_id)
    await callback.message.answer(text='ID',
                                  reply_markup=cancel_keyboard)
    await callback.message.delete()
    await callback.answer()


@router.message(AddGSState.GS_id)
async def set_gs_id(message: Message, state: FSMContext):
    await state.update_data(gs_id=message.text)
    await state.set_state(AddGSState.GS_name)
    await message.answer('NAME')


@router.message(AddGSState.GS_name)
async def set_gs_id(message: Message, state: FSMContext):
    await state.update_data(gs_name=message.text)
    await state.set_state(AddGSState.GS_description)
    await message.answer('DESC')


@router.message(AddGSState.GS_description)
async def set_gs_id(message: Message, state: FSMContext):
    await state.update_data(gs_description=message.text)
    gs_data = await state.get_data()
    print(f'id: {gs_data.get("gs_id")} | name: {gs_data.get("gs_name")} | desc: {gs_data.get("gs_description")}')
    await state.clear()
    await message.answer('УСПЕХ', reply_markup=admin_panel_keyboard)

