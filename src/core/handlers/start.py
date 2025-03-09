from aiogram import Router, types
from aiogram.filters import CommandStart

from core.keyboards import InlineKeyboard as Inline

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "Hello! I'm a Bot",
        reply_markup=Inline.locale_language()
    )
