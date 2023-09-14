from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards.gs.av.keyboard_gs_av import gs_av_keyboard
from keyboards.gs.av.keyboard_back_to_period import gs_keyboard

router: Router = Router()


@router.callback_query(F.data == 'gs-av')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text='ГС для Аудио-Видео техники.\nВыберите действие', reply_markup=gs_av_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-av-premium-plus-12')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text="""
    <b>1</b>\n
    """, reply_markup=gs_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-av-repeat-12')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text="""
    <b>2</b>\n
    """, reply_markup=gs_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-av-premium-plus-36')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text="""
    <b>3</b>\n
    """, reply_markup=gs_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-av-premium-plus-48')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text="""
    <b>4</b>\n
    """, reply_markup=gs_keyboard)
    await callback.answer()
