from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from keyboards.default import main_menu, location_menu
from loader import dp
from states import UserProfile
from utils.db import User


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, user: User):
    await message.answer(
        f'Привет, {message.from_user.full_name}! \n'
        f'Middleware {user.full_name} \n'
        f'Отправь свою геолокацию, чтобы я показал тебе погоду:',
        reply_markup=location_menu
    )
    await UserProfile.first()


@dp.message_handler(content_types=types.ContentTypes.LOCATION, state=UserProfile.location)
async def get_location(message: types.Message, state: FSMContext):
    await state.update_data(location={
        'lon': message.location.longitude,
        'lat': message.location.latitude
    })
    await message.answer(
        text=f'thx \n'
             f'longitude: {message.location.longitude} \n'
             f'latitude: {message.location.latitude}',
        reply_markup=main_menu
    )
    await state.reset_state(False)
