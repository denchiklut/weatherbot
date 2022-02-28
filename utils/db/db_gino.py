from gino import Gino
from aiogram import Dispatcher
import config

db = Gino()


async def on_startup(dispatcher: Dispatcher):
    await db.set_bind(config.db_uri, loop=dispatcher.loop)
