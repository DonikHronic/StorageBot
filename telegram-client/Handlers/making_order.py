import json

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from Keyboards.inline.callback_datas import order, buy_cart, close_order
from States.cart_state import CartState
from States.make_order import MakeOrder
from Utils.commands import ERROR_LIST
from Utils.get_request_header import get_request_header
from config import URI
from loader import dp


@dp.callback_query_handler(order.filter(value='add_to_cart'), state=None)
async def add_to_cart(call: CallbackQuery, state: FSMContext):
	text = call.message.caption
	product_id = int(text[0])
	await state.update_data(product=product_id)
	await call.message.answer('Set count')
	await CartState.set_count.set()


@dp.message_handler(state=CartState.set_count)
async def set_cart_count(message: types.Message, state: FSMContext):
	try:
		count = int(message.text)
		state_data = await state.get_data()
		product = state_data['product']
		header = await get_request_header(message.from_user)
		cart_item = {
			'product': product,
			'count': count
		}
		await state.finish()
		response = requests.post(headers=header, url=f'{URI}bot/add-to-cart/', data=cart_item)
		if response.status_code == 201:
			await message.answer('Продукт добавлен в корзину')
		else:
			await message.answer(ERROR_LIST['general_fail'])
	except ValueError:
		await message.answer(ERROR_LIST['fail_count'])


@dp.callback_query_handler(buy_cart.filter(value='buy'), state=None)
async def set_location(call: CallbackQuery, state: FSMContext):
	await call.message.answer("Куда доставить надо?")
	await MakeOrder.location.set()


@dp.message_handler(state=MakeOrder.location)
async def make_order(message: types.Message, state: FSMContext):
	location = message.text
	header = await get_request_header(message.from_user)
	order_data = {'location': location}
	response = requests.post(headers=header, data=order_data, url=f'{URI}bot/make-order/')
	if response.status_code == 201:
		await message.answer('Заявка оформлена')
		await state.finish()
	else:
		await message.answer(ERROR_LIST['general_fail'])


@dp.callback_query_handler(buy_cart.filter(value='clean'), state=None)
async def clean_cart(call: CallbackQuery, state: FSMContext):
	header = await get_request_header(call.from_user)

	response = requests.delete(headers=header, url=f'{URI}bot/clear-cart/')
	if response.status_code == 200:
		await call.message.answer('Корзина очищена')
	else:
		await call.message.answer(ERROR_LIST['general_fail'])


@dp.callback_query_handler(close_order.filter(value='close'), state=None)
async def confirm_order(call: CallbackQuery, state: FSMContext):
	header = await get_request_header(call.from_user)
	order_id = call.message.text[-1]
	statuses = json.loads(requests.get(url=f'{URI}bot/get-status-list/').text)
	print()
	data = {
		'order': int(order_id),
		'status': statuses[-1][0]
	}

	response = requests.put(url=f'{URI}bot/update-order/', data=data, headers=header)
	if response.status_code == 202:
		await call.message.answer('Заявка закрыта')
	else:
		await call.message.answer(ERROR_LIST['general_fail'])
