from aiogram.fsm.state import StatesGroup, State


class AddGSState(StatesGroup):
    GS_id = State()
    GS_name = State()
    GS_description = State()
