from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_client = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="Оставить заявку"),
			KeyboardButton(text="Просмотреть мои заявки")
		],
		[
			KeyboardButton(text="Связаться с закупщиком")
		]
	],
	resize_keyboard=True
)
