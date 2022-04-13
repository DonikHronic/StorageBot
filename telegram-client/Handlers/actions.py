import json

import requests
from aiogram import types
from aiogram.utils.exceptions import MessageTextIsEmpty

from Keyboards.inline.cart_buy import buy_cart
from Keyboards.inline.close_order import close
from Keyboards.inline.product_btns import product_buy
from Utils.commands import MENU_COMMANDS
from Utils.get_request_header import get_request_header
from config import URI
from loader import dp


@dp.message_handler(text=MENU_COMMANDS['add_order'])
async def show_products(message: types.Message):
	""""""
	header = await get_request_header(message.from_user)
	response = requests.get(headers=header, url=f'{URI}bot/products/')
	products = json.loads(response.text)
	for product in products:
		product_info = f'{product["id"]}. Название: {product["name"]}\nЦена: {product["price"]}'
		image_url = 'https://upload.wikimedia.org/wikipedia/commons/7/78/Image.jpg'
		await message.answer_photo(photo=image_url, caption=product_info, reply_markup=product_buy)
	await message.answer('Добавьте продукт в корзину затем через корзину оформите заявку')


@dp.message_handler(text=MENU_COMMANDS['my_cart'])
async def my_cart(message: types.Message):
	""""""
	header = await get_request_header(message.from_user)
	response = requests.get(headers=header, url=f'{URI}bot/get_cart/')
	products = json.loads(response.text)
	message_text = ''
	for i, product in enumerate(products):
		text = f'''{i + 1}. {product["product"]["name"]}
Кол-во: {product["count"]}, Цена: {product["product"]["price"] * product["count"]}\n'''
		message_text += text

	try:
		await message.answer(message_text, reply_markup=buy_cart)
	except MessageTextIsEmpty:
		await message.answer("Корзина пуста")


@dp.message_handler(text=MENU_COMMANDS['my_orders'])
async def my_orders(message: types.Message):
	""""""
	header = await get_request_header(message.from_user)
	response = requests.get(url=f'{URI}bot/my-orders/', headers=header)
	statuses = json.loads(requests.get(url=f'{URI}bot/get-status-list/').text)
	orders = json.loads(response.text)
	statuses = dict(statuses)

	if not orders:
		await message.answer('У вас нет заявок')
		return

	for order in orders:
		order_text = ''
		for product in order['products']:
			order_text += f'Продукт: {product["name"]}, Цена: {product["price"]}\n'
		order_text += f'Окончательная цена: {order["total_price"]}\n'
		order_text += f'Адрес доставки: {order["location"]}\n'
		order_text += f'Статус заявки: {statuses.get(order["status"])}\n'
		order_text += f'{order["detail"]}\n'
		order_text += f'Номер заказа: {order["id"]}'

		if order['status'] == 'SUBMITTED':
			await message.answer(order_text, reply_markup=close)
		else:
			await message.answer(order_text)
