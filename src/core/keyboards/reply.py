from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class ReplyKeyboard:
    @staticmethod
    def menu() -> ReplyKeyboardMarkup:
        builder = ReplyKeyboardBuilder()
        builder.button(text="")
        ...
        builder.adjust(...)
        return builder.as_markup(resize_keyboard=True)
