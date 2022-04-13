from aiogram.utils import executor

from Controllers.SetCommands import DefaultCommands
from Utils.commands import INFO_LIST
from loader import bot, admin_id, bot_logger, configure_logger, dp
import Middlewares, Handlers


async def on_startup(dispatcher):
	await DefaultCommands().set_default_commands(dispatcher)
	await bot.send_message(admin_id, f'<i>{INFO_LIST["bot_started"]}</i>')
	bot_logger.info('Bot started')

if __name__ == '__main__':
	configure_logger()
	executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
