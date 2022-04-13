from aiogram import types
from aiogram.dispatcher.filters import Command

from Utils.commands import INFO_LIST
from loader import dp


@dp.message_handler(Command('help'))
async def help_command(message: types.Message):
	await message.answer(INFO_LIST["show_actions"])
