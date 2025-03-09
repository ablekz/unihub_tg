from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class InlineKeyboard:
    @staticmethod
    def locale_language() -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()
        builder.button(text="🇺🇸", callback_data="locale_en")
        builder.button(text="🇷🇺", callback_data="locale_ru")
        builder.button(text="🇰🇿", callback_data="locale_kz")
        builder.adjust(3)
        return builder.as_markup()
