from aiogram import types
from aiogram.dispatcher.filters import CommandHelp
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_start(message: types.Message):
    await message.answer('Этот бот поможет узнать погоду')
