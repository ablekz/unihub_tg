from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from settings import get_settings

settings = get_settings()

bot = Bot(token=settings.BOT_TOKEN,
          default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()
