from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from utils.db.schemas import User
from keyboards.default import main_menu
from states import UserProfile


@dp.message_handler(content_types=types.ContentTypes.LOCATION, state=UserProfile.location)
async def get_location(message: types.Message, state: FSMContext):
    await User.create(
        id=message.from_user.id,
        longitude=message.location.longitude,
        latitude=message.location.latitude
    )
    await state.finish()
    await message.answer(
        text='Вот спсиок того что я умею',
        reply_markup=main_menu
    )
