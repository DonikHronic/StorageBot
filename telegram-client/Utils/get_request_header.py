from aiogram.types import User

from Utils.authorization import authorize


async def get_request_header(user: User):
	token = await authorize(user)
	return {"Authorization": f"Bearer {token['access']}"}
