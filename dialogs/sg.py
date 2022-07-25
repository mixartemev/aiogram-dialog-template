from aiogram.dispatcher.filters.state import StatesGroup, State


class MainSG(StatesGroup):
    set_opponent = State()
    invite_link = State()
    options = State()
    waiting_for_join = State()
    waiting_for_choise = State()
    solved = State()
