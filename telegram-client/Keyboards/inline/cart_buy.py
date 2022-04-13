from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

buy_cart = InlineKeyboardMarkup(row_width=2)

buy = InlineKeyboardButton(text='Оформить заявку', callback_data='action:buy')
clean = InlineKeyboardButton(text='Очистить корзину', callback_data='action:clean')

buy_cart.insert(buy)
buy_cart.insert(clean)
