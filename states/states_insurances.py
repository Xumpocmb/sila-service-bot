from aiogram.fsm.state import StatesGroup, State


class MobilePriceState(StatesGroup):
    set_mobile_price = State()


class BikePriceState(StatesGroup):
    set_bike_price = State()


class YourselfPriceState(StatesGroup):
    set_mobile_price = State()
    set_month_count = State()
