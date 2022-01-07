import json

import requests
from aiogram import types


async def registrate(user: types.user.User):
	user_data = {
		"username": f"{user.first_name}{user.id}",
		"password": f"user_pass_{user.id}",
		"fullname": f"{user.first_name} {user.last_name}",
		"telegram_id": user.id,
		"role": "C"
	}

	response = requests.post(url='http://localhost:8080/api/v1/bot/client-registration/', data=user_data)
	return response


async def authorize(user: types.user.User) -> dict:
	user_data = {
		"username": f"{user.first_name}{user.id}",
		"password": f"user_pass_{user.id}",
	}
	token = requests.post(url='http://localhost:8080/api/v1/auth/jwt/create/', data=user_data).text
	token = json.loads(token)

	if token:
		return token
	else:
		registration = await registrate(user)

	if registration.status_code == 201:
		return await authorize(user)
