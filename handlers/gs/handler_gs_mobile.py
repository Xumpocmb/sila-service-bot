from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards.gs.mobile.keyboard_gs_mobile import gs_mobile_keyboard
from keyboards.gs.mobile.keyboard_back_to_period import gs_keyboard

router: Router = Router()


@router.callback_query(F.data == 'gs-mobile')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text='ГС для мобильных устройств.\nВыберите действие', reply_markup=gs_mobile_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-mobile-12')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text="""
    ГС 12 для мобильных устройств.\n
    ГарантСервис Премиум Плюс на 12 месяцев для Мобильных Устройств:\n
    Ремонт в негарантийных случаях, даже при механических повреждениях и попадании влаги\n
    Стартовая диагностика устройства\n
    Установка блокировщика рекламы, с лицензией на 1 год\n
    Установка приложения EYESPRO, лицензия на 6 мес, которое обеспечивает защиту глаз (доступно для ОС Android)\n
    Услуга по наклейке защитной плёнки/стекла на устройство (плёнка/стекло предоставляется клиентом)\n
    Онлайн поддержка 24/7, 1 месяц\n
    """, reply_markup=gs_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-mobile-24')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text="""
    <b>ГС 24 для мобильных устройств.</b>\n
    ГарантСервис Премиум Плюс на 24 месяцев для Мобильных Устройств:\n
    Ремонт в негарантийных случаях(перепады напряжения, естественный износ,производственный дефект за пределами заводской гарантии), даже при механических повреждениях и попадании влаги(первые 12 мес)\n
    Стартовая диагностика устройства\n
    Установка блокировщика рекламы, с лицензией на 1 год\n
    Установка антивирусной защиты Kaspersky 1 год 1 устройство(доступно для ОС Android)\n
    Услуга по наклейке защитной плёнки Anticrash Глянец\n
    Онлайн поддержка 24/7 (1 мес)\n
    """, reply_markup=gs_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-mobile-repeat-12')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text="""
    <b>ГарантСервис Повторный на 12 месяцев для Мобильных Устройств:</b>\n
    Ремонт в негарантийных случаях, даже при механических повреждениях и попадании влаги\n
    Установка блокировщика рекламы, с лицензией на 1 год\n
    Установка приложения EYESPRO, лицензия на 6 мес, которое обеспечивает защиту глаз (доступно для ОС Android)\n
    Услуга по наклейке защитной плёнки/стекла на устройство (плёнка/стекло предоставляется клиентом)\n
    Онлайн поддержка 24/7(1 мес)\n
    """, reply_markup=gs_keyboard)
    await callback.answer()
