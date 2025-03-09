from motor.motor_asyncio import AsyncIOMotorClient
from settings import get_settings

settings = get_settings()


class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.MONGODB_URI)
        self.db = self.client.get_database()


db = Database()
