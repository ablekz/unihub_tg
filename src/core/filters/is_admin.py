from aiogram.filters import BaseFilter
from aiogram.types import Message
from settings import get_settings

settings = get_settings()


class IsAdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in settings.ADMINS
