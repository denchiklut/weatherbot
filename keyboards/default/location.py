from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

location_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📍 Отправить геолокацию', request_location=True)]
    ],
    resize_keyboard=True
)
