from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

close = InlineKeyboardMarkup(row_width=1)
btn = InlineKeyboardButton(text='Подтвердить получение', callback_data='action:close')
close.insert(btn)
