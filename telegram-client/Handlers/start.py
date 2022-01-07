from aiogram import types
from aiogram.dispatcher.filters import Command

from Utils.auth import authorize
from loader import dp


@dp.message_handler(Command('start'))
async def start_command(message: types.Message):
	token = await authorize(message.from_user)
	await message.answer('Authenticated')
