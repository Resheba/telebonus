from aiogram import Bot, Dispatcher
from loguru import logger

from src.config import Settings
from src.sheet import SheetService

from .services import bonus_router


class Telegram:
    def __init__(self, token: str) -> None:
        self._bot = Bot(token=token)
        self._dp = Dispatcher()

    @classmethod
    def from_settings(cls, settings: Settings) -> "Telegram":
        return cls(token=settings.TELEGRAM_TOKEN)

    async def start(self, sheet_service: SheetService) -> None:
        logger.info("Starting bot...")
        self._dp.include_routers(bonus_router)
        await self._dp.start_polling(self._bot, sheet_service=sheet_service)
