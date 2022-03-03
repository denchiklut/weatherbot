from aiogram import types
from loader import dp
from keyboards.default import main_menu
from utils.weather import get_current, conditions


@dp.message_handler(text='🌤 Погода сейчас')
async def get_now(message: types.Message, user):
    weather = await get_current(user.latitude, user.longitude)

    description = conditions[weather['fact']['condition']]
    temperature = round(weather['fact']['temp'])
    location = f"{weather['geo_object']['country']['name']}, {weather['geo_object']['province']['name']} - {weather['geo_object']['district']['name']}"

    await message.answer(
        text=f'Темпиратура: {round(temperature)} \n'
             f'Описание: {description} \n'
             f'Локация: {location}',
        reply_markup=main_menu
    )
