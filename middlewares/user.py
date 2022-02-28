from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from utils.db import User


class CurrentUser(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        data['user'] = await User.query.where(User.id == message.from_user.id).gino.first()
