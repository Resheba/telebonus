from pathlib import Path
from typing import TYPE_CHECKING

from src.config import Settings

from .reader import Reader
from .schemas import User

if TYPE_CHECKING:
    from gspread.worksheet import Worksheet


class SheetService:
    _user_list_name: str = Settings.LIST_USERS
    _user_name_col: int = Settings.USER_NAME_COL
    _user_tid_col: int = Settings.USER_TID_COL

    def __init__(self, secret_filename: str | Path, sheet_key: str) -> None:
        self._reader: Reader = Reader(
            secret_filename=secret_filename,
            sheet_key=sheet_key,
        )

    def get_users(self) -> tuple[User, ...]:
        worksheet: Worksheet = self._reader.worksheet(self._user_list_name)
        names: list[int | float | str | None] = worksheet.col_values(self._user_name_col)
        ids: list[int | float | str | None] = worksheet.col_values(self._user_tid_col)
        return tuple(
            User(telegram_id=str(tid), name=str(name))
            for name, tid in zip(names, ids, strict=False)
        )
