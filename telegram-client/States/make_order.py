from aiogram.dispatcher.filters.state import StatesGroup, State


class MakeOrder(StatesGroup):
	location = State()
