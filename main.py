from aiogram import Dispatcher
from utils.db import db_gino
from loader import db


async def on_startup(dispatcher: Dispatcher):
    await db_gino.on_startup(dispatcher)
    await db.gino.create_all()

    from utils.commands import set_commands
    import middlewares

    middlewares.setup(dispatcher)
    await set_commands(dispatcher)


if __name__ == '__main__':
    from aiogram import executor, Dispatcher
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
