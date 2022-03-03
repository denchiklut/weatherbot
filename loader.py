from aiohttp import ClientSession
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from config import token
from utils.db.db_gino import db

bot = Bot(token)

storage = MemoryStorage()
session = ClientSession()
dp = Dispatcher(bot, storage=storage)

__all__ = ['bot', 'storage', 'dp', 'db', 'session']
