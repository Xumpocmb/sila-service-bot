from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards.gs.computer.keyboard_gs_computer import gs_computer_keyboard
from keyboards.gs.computer.keyboard_back_to_period import gs_keyboard

router: Router = Router()


@router.callback_query(F.data == 'gs-computer')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text='ГС для компьютерной техники.\nВыберите действие', reply_markup=gs_computer_keyboard)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'gs-computer-24')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text="""
    <b>ГС на 24 мес. для комп. техники</b>\n
    Ремонт по окончанию основной гарантии\n
    Ремонт в негарантийных случаях. Даже при поломках от перепадов напряжения, механических повреждений и попадания влаги(1 раз в течении действия договора,  после ГарантСервис прекращает действия договора)\n
    Онлайн поддержка 24/7,2 мес\n
    Для ноутбуков, нетбуков, моноблоков, системных блоков в пакет входят профилактические работы, продлевающие срок службы(1 профилактика,воспользоваться можно не раньше чем через год с момента покупки)\n
    """, reply_markup=gs_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-computer-premium-24')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text="""
    <b>ГС Премиум на 24 мес. для комп. техники</b>\n
    Ремонт по окончанию основной гарантии\n
    Ремонт в негарантийных случаях. Даже при поломках от перепадов напряжения, механических повреждений и попадания влаги(1 раз в течении действия договора,  после ГарантСервис прекращает действия договора)\n
    Онлайн поддержка 24/7,2 мес\n
    Установка антивируса Kaspersky, годовая лицензия для 3-х устройств\n
    Для ноутбуков, нетбуков, моноблоков, системных блоков в пакет входят профилактические работы, продлевающие срок службы(1 профилактика,воспользоваться можно не раньше чем через год с момента покупки)\n
    """, reply_markup=gs_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-computer-36')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text="""
    <b>ГС на 36 мес. для комп. техники</b>\n
    Ремонт по окончанию основной гарантии\n
    Ремонт в негарантийных случаях. Даже при поломках от перепадов напряжения, механических повреждений и попадания влаги(1 раз в течении действия договора, после ГарантСервис прекращает действия договора)\n
    Онлайн поддержка 24/7,2 мес\n
    Для ноутбуков, нетбуков, моноблоков, системных блоков в пакет входят профилактические работы, продлевающие срок службы(2 профилактики,первый раз не раньше чем через год с момента покупки)\n
    """, reply_markup=gs_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-computer-premium-36')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text="""
    <b>ГС Премиум на 36 мес. для комп. техники</b>\n
    Ремонт по окончанию основной гарантии\n
    Ремонт в негарантийных случаях. Даже при поломках от перепадов напряжения, механических повреждений и попадания влаги(1 раз в течении действия договора, после ГарантСервис прекращает действия договора)\n
    Онлайн поддержка 24/7,2 мес\n
    Установка антивируса Kaspersky, годовая лицензия для 3-х устройств\n
    Для ноутбуков, нетбуков, моноблоков, системных блоков в пакет входят профилактические работы, продлевающие срок службы(2 профилактики,первый раз не раньше чем через год с момента покупки)\n
    """, reply_markup=gs_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-computer-repeat-24')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text="""
    <b>ГС Повторный на 24 мес. для комп. техники</b>\n
    Оформляется по истечению срока действия или после ремонта, связанным с нарушением Правил и условий эксплуатации\n
    Ремонт в негарантийных случаях. Даже при поломках от перепадов напряжения, механических повреждений и попадания влаги(1 раз в течении действия договора,  после ремонта ГарантСервис прекращает действовать)\n
    Онлайн поддержка 24/7,2 мес\n
    Для ноутбуков, нетуков, моноблоков, системных блоков в пакет входят профилактические работы, продлевающие срок службы(1 профилактика,воспользоваться можно не раньше чем через год с момента покупки)\n
    """, reply_markup=gs_keyboard)
    await callback.answer()
