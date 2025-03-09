import logging
from settings import get_settings

settings = get_settings()

logging.basicConfig(
    level=settings.LOG_LEVEL,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("unihub.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("unihub")
logger.info("Logging stared!")
