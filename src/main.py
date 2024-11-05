from loguru import logger

from src.config import Settings
from src.sheet import SheetService


def main() -> None:
    service: SheetService = SheetService(
        secret_filename=Settings.SERVICE_ACCOUNT_PATH,
        sheet_key=Settings.SHEET_KEY,
    )
    logger.info(service.get_users())


if __name__ == "__main__":
    main()
