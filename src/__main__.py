import asyncio

from core.logger import logger
from database.db import db
from settings import get_settings
from bot import bot, dp
from dispatcher import register_handlers

settings = get_settings()


async def main():
    logger.info("Bot started")
    logger.info("Connecting to the database...")

    try:
        await db.client.admin.command("ping")  # Check connection to MongoDB
        logger.info("MongoDB connected successfully")
    except Exception as e:
        logger.critical(f"Error connecting to MongoDB: {e}")
        return

    register_handlers(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
