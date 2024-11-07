from asyncio import run

from loguru import logger

from src.config import Settings
from src.sheet import SheetService
from src.telegram import Telegram


async def main() -> None:
    settings: Settings = Settings.get_settings()
    # telegram: Telegram = Telegram.from_settings(settings=settings)
    service: SheetService = SheetService.from_settings(settings=settings)
    bonus = service.get_bonus_by_tid(tid="5")
    service.inject_bonus_projects(bonus=bonus)
    logger.info(bonus.bonuses)
    # await telegram.start(sheet_service=service)


if __name__ == "__main__":
    run(main())
