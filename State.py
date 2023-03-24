from aiogram.dispatcher.filters.state import StatesGroup, State
class ProfileStatesGroup(StatesGroup):
    photo = State()
    audio = State()
