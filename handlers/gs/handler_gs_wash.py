from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards.gs.wash.keyboard_gs_wash import gs_wash_keyboard
from keyboards.gs.wash.keyboard_back_to_period import gs_keyboard

router: Router = Router()


@router.callback_query(F.data == 'gs-wash')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text='ГС для мобильных устройств.\nВыберите действие', reply_markup=gs_wash_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-wash-36')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text="""
    <b>ГарантСервис на 36 месяцев для стиральных, посудомоечных и сушильных машин.</b>\n
    Ремонт по окончанию основной гарантии\n
    Ремонт в негарантийных случаях, даже при поломках от перепадов напряжения(1ый год ремонт при Нарушений правил и условий эксплуатации)\n
    В пакет входит организация профилактических работ для продления срока службы техники (чистка фильтров грубой и тонкой очистки, очистка от накипи бака барабана и нагревательного элемента спец. средствами, проверка герметизации соединений и т.д.)(первый раз после 6 мес с момента покупки)\n
    Онлайн поддержка 24/7 (1 мес)\n
    """, reply_markup=gs_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-wash-48')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text="""
    <b>ГС на 48 месяцев для стиральных, посудомоечных и сушильных машин.</b>\n
    Ремонт по окончанию основной гарантии\n
    Ремонт в негарантийных случаях, даже при поломках от перепадов напряжения(1ый год ремонт при Нарушений правил и условий эксплуатации)\n
    В пакет входит организация профилактических работ для продления срока службы техники (чистка фильтров грубой и тонкой очистки, очистка от накипи бака барабана и нагревательного элемента спец. средствами, проверка герметизации соединений и т.д.)(первый раз после 6 мес с момента покупки)\n
    Онлайн поддержка 24/7 (1 мес)\n
    """, reply_markup=gs_keyboard)
    await callback.answer()


@router.callback_query(F.data == 'gs-wash-60')
async def send_t_shirt(callback: CallbackQuery):
    await callback.message.answer(text="""
    <b>ГарантСервис на 60 месяцев для стиральных, посудомоечных и сушильных машин.</b>\n
    Установка Стандарт(не входит отключение и демонтаж техники)\n
    Ремонт по окончанию основной гарантии\n
    Ремонт в негарантийных случаях, даже при поломках от перепадов напряжения(1ый год ремонт при Нарушений правил и условий эксплуатации)\n
    В пакет входит организация профилактических работ для продления срока службы техники (чистка фильтров грубой и тонкой очистки, очистка от накипи бака барабана и нагревательного элемента спец. средствами, проверка герметизации соединений и т.д.)(первый раз после 6 мес с момента покупки)\n
    Онлайн поддержка 24/7 (1 мес)\n
    """, reply_markup=gs_keyboard)
    await callback.answer()
