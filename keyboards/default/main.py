from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('🌤 Погода сейчас'),
            KeyboardButton(' 🌅 На завтра')
        ],
        [
            KeyboardButton('🔮 На 5 дней'),
            KeyboardButton('🔮 На 10 дней')
        ],
        [
            KeyboardButton('⚙️ Настройки')
        ]
    ],
    resize_keyboard=True
)
