from aiogram import Dispatcher
from .user import CurrentUser


def setup(db: Dispatcher):
    db.middleware.setup(CurrentUser())
