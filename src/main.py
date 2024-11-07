from asyncio import run

from loguru import logger

from src.config import Settings
from src.sheet import SheetService
from src.telegram import Telegram


async def main() -> None:
    settings: Settings = Settings.get_settings()
    telegram: Telegram = Telegram.from_settings(settings=settings)
    await telegram.start()
    # service: SheetService = SheetService.from_settings(settings=settings)
    # logger.info(service.get_bonus_by_tid(tid="1"))
    # logger.info(service.get_bonus_by_tid(tid="2"))
    # logger.info(service.get_bonus_by_tid(tid="14677"))


if __name__ == "__main__":
    run(main())
