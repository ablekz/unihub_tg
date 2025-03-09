from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from core.filters import IsAdminFilter

router = Router()
router.message.filter(IsAdminFilter())


@router.message(Command("admin"))
async def admin_panel(message: Message):
    await message.answer("Welcome to Admin Panel!")
