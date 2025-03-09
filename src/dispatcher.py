from aiogram import Dispatcher
from core.handlers import start, help, admin, user


def register_handlers(dp: Dispatcher):
    dp.include_routers(
        start.router,
        help.router,
        admin.router,
        user.router
    )
