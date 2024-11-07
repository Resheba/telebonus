from asyncio import run

from src.config import Settings
from src.sheet import SheetService
from src.telegram import Telegram


async def main() -> None:
    settings: Settings = Settings.get_settings()
    telegram: Telegram = Telegram.from_settings(settings=settings)
    service: SheetService = SheetService.from_settings(settings=settings)
    await telegram.start(sheet_service=service)


if __name__ == "__main__":
    run(main())
