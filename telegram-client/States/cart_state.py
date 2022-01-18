from aiogram.dispatcher.filters.state import StatesGroup, State


class CartState(StatesGroup):
	set_count = State()