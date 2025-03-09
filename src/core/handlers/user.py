from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("user"))
async def help_handler(message: types.Message):
    await message.answer("User")
