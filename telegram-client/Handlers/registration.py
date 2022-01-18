from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from Keyboards.default.menu import menu_client
from Keyboards.inline.callback_datas import user_choice
from Utils.authorization import registrate
from Utils.commands import ERROR_LIST
from loader import dp


@dp.callback_query_handler(user_choice.filter(), state=None)
async def registration(call: CallbackQuery, state: FSMContext):
	user = call.from_user
	try:
		reg_response = await registrate(user, call.data[-1])
		if reg_response.status_code == 201 and call.data[-1] == 'C':
			await call.message.answer('Registration Complete', reply_markup=menu_client)
		elif reg_response.status_code == 201:
			await call.message.answer(
				f'You authorized in system. Your username = {user.first_name}{user.id}, password = user_pass_{user.id}'
			)
		else:
			await call.answer(ERROR_LIST['fail_registration'])
	except ValueError:
		await call.answer(ERROR_LIST['fail_registration'])
