from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from loguru import logger

from src.config import Settings

router: Router = Router(name="Bonus")
settings: Settings = Settings.get_settings()


@router.message(CommandStart())
async def start_command(message: Message) -> None:
    await message.reply(
        f"Привет{', ' + message.chat.full_name if message.chat.first_name else ''}!\n"
        "Доступные команды:"
        f"\n📍\t/{settings.TELEGRAM_ME_COMMAND}\n📍\t/{settings.TELEGRAM_COMMON_COMMAND}",
    )


@router.message(Command(settings.TELEGRAM_ME_COMMAND))
async def me_command(message: Message) -> None:
    chat_id: int = message.chat.id
    ...


@router.message(Command(settings.TELEGRAM_COMMON_COMMAND))
async def common_command(message: Message) -> None: ...
