from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import token

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
