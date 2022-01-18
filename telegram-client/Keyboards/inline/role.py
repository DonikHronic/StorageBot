from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Utils.commands import INFO_LIST

choice = InlineKeyboardMarkup(row_width=2)

add_client = InlineKeyboardButton(text=INFO_LIST['client'], callback_data='registration:C')
add_buyer = InlineKeyboardButton(text=INFO_LIST['buyer'], callback_data='registration:E')

choice.insert(add_client)
choice.insert(add_buyer)
