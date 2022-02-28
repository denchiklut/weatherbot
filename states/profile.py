from aiogram.dispatcher.filters.state import StatesGroup, State


class UserProfile(StatesGroup):
    location = State()
