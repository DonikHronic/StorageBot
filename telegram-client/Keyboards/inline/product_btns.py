from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

product_buy = InlineKeyboardMarkup(row_width=2)

add_to_cart = InlineKeyboardButton(text='В корзину', callback_data='action:add_to_cart')

product_buy.insert(add_to_cart)
