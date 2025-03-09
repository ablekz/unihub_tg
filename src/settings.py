from pydantic_settings import BaseSettings
from pydantic import field_validator
from functools import lru_cache


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMINS: list[int]
    MONGODB_URI: str
    LOG_LEVEL: str = "INFO"


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()
