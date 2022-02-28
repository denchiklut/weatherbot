from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from utils.db import User


class CurrentUser(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        data['user'] = User(user_id=message.from_user.id, full_name=message.from_user.full_name)
