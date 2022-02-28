from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from keyboards.default import main_menu, location_menu
from states import UserProfile
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, user):
    if user:
        await message.answer(
            text='Вот спсиок того что я умею',
            reply_markup=main_menu
        )
    else:
        await message.answer(
            f'Привет, {message.from_user.full_name}! \n'
            f'Отправь свою геолокацию, чтобы я показал тебе погоду:',
            reply_markup=location_menu
        )
        await UserProfile.first()
