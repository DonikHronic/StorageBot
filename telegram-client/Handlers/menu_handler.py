from aiogram import types
from aiogram.dispatcher.filters import Command

from Keyboards.default.menu import menu_client
from loader import dp


@dp.message_handler(Command('menu'))
async def menu(message: types.Message):
	await message.answer('Выберите действия из меню ниже', reply_markup=menu_client)
