import json

import requests
from aiogram import types

from config import URI


async def registrate(user: types.user.User, role: str):
	user_data = {
		"username": f"{user.first_name}{user.id}",
		"password": f"user_pass_{user.id}",
		"fullname": f"{user.first_name} {user.last_name}",
		"telegram_id": user.id,
		"role": role
	}
	if role == 'E':
		return requests.post(url=f'{URI}bot/employee-registration/', data=user_data)
	elif role == 'C':
		return requests.post(url=f'{URI}bot/client-registration/', data=user_data)
	else:
		raise ValueError


async def authorize(user: types.user.User) -> dict:
	user_data = {
		"username": f"{user.first_name}{user.id}",
		"password": f"user_pass_{user.id}",
	}
	token = requests.post(url=f'{URI}auth/jwt/create/', data=user_data).text
	token = json.loads(token)

	return token
