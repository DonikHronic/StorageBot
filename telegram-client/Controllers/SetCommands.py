from aiogram import Dispatcher, types


class DefaultCommands:
	commands_list = [
		('start', 'Запустить бота'),
		('help', 'Помощь'),
		('menu', 'Список действий'),
	]

	async def set_default_commands(self, dispatcher: Dispatcher):
		commands = [types.BotCommand(command, description) for command, description in self.commands_list]
		await dispatcher.bot.set_my_commands(commands)