from aiogram import Bot, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from loguru import logger

from src.config import Settings
from src.sheet import Bonus, SheetService
from src.sheet.exception import SheetBonusNotFoundError, SheetNotFoundError, SheetUserNotFoundError

router: Router = Router(name="Bonus")
settings: Settings = Settings.get_settings()


@router.message(CommandStart())
async def start_command(message: Message) -> None:
    await message.answer(
        f"Привет{', ' + message.chat.full_name if message.chat.first_name else ''}!\n"
        "Доступные команды:"
        f"\n📍\t/{settings.TELEGRAM_ME_COMMAND}",
    )


@router.message(Command(settings.TELEGRAM_ME_COMMAND))
async def me_command(message: Message, bot: Bot, sheet_service: SheetService) -> None:
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    try:
        bonus: Bonus = sheet_service.get_bonus_by_tid(tid=str(message.chat.id))
    except SheetUserNotFoundError:
        await message.reply("❌\tНе нашёл Вас в таблице.")
    except SheetNotFoundError:
        await message.reply("❌\tОшибка при получении таблицы.")
    except SheetBonusNotFoundError:
        await message.reply("❌\tНе нашёл Ваш бонус.")
    except Exception as ex:  # noqa: BLE001
        await message.reply("❌\tПроизошла ошибка.")
        logger.exception(ex)
    else:
        await message.answer(
            f"✅\tВаш бонус, {bonus.username}:\n"
            f"📍\tKPI: {bonus.kpi}\n"
            f"📍\tВсего: {bonus.amount}",
        )
