from aiogram import types
from aiogram.dispatcher.filters import Command

from Keyboards.inline.role import choice
from loader import dp


@dp.message_handler(Command('start'))
async def start_command(message: types.Message):
	await message.answer('Бот для заявок. Пожалуйста укажите кто вы, для дальнейших действий', reply_markup=choice)
