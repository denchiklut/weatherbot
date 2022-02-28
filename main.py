from aiogram import Dispatcher


async def on_startup(dispatcher: Dispatcher):
    from utils.commands import set_commands
    import middlewares

    middlewares.setup(dispatcher)
    await set_commands(dispatcher)


if __name__ == '__main__':
    from aiogram import executor, Dispatcher
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
