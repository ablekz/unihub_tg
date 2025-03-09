from aiogram.types import Update
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from database.db import db
from utils.translator import set_locale


class LanguageMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Update, data: dict):
        user_id = event.from_user.id
        user = await db.students.find_one({"user_id": user_id})

        if user and "language" in user:
            set_locale(user["language"])  # Change the language

        return await handler(event, data)
