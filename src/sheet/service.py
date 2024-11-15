from pathlib import Path
from typing import TYPE_CHECKING, Self

from gspread.utils import a1_range_to_grid_range, rowcol_to_a1
from loguru import logger

from src.config import Settings

from .exception import SheetBonusNotFoundError, SheetUserNotFoundError
from .reader import Reader
from .schemas import Bonus, BonusProject, User

if TYPE_CHECKING:
    from gspread.cell import Cell
    from gspread.worksheet import Worksheet


class SheetService:
    def __init__(
        self,
        secret_filename: str | Path,
        sheet_key: str,
        user_list_name: str,
        user_name_range: str,
        user_tid_range: str,
        current_list_name: str,
        current_bonus_range: str,
        current_kpi_range: str,
        current_names_range: str,
        current_bonus_pj_names_range: str,
    ) -> None:
        self._user_list_name: str = user_list_name
        self._user_name_range: str = user_name_range
        self._user_tid_range: str = user_tid_range

        self._current_list_name: str = current_list_name
        self._current_bonus_range: str = current_bonus_range
        self._current_kpi_range: str = current_kpi_range
        self._current_names_range: str = current_names_range
        self._current_bonus_pj_names_range: str = current_bonus_pj_names_range
        self._current_bonus_pj_start_row: int = a1_range_to_grid_range(
            self._current_bonus_pj_names_range,
        ).get("startRowIndex", 0)

        self._reader: Reader = Reader(
            secret_filename=secret_filename,
            sheet_key=sheet_key,
        )

    @classmethod
    def from_settings(cls, settings: Settings) -> Self:
        return cls(
            secret_filename=settings.SERVICE_ACCOUNT_PATH,
            sheet_key=settings.SHEET_KEY,
            user_list_name=settings.LIST_USERS,
            user_name_range=settings.USER_NAME_RANGE,
            user_tid_range=settings.USER_TID_RANGE,
            current_list_name=settings.LIST_CURRENT,
            current_bonus_range=settings.CURRENT_BONUS_RANGE,
            current_kpi_range=settings.CURRENT_KPI_RANGE,
            current_names_range=settings.CURRENT_NAMES_RANGE,
            current_bonus_pj_names_range=settings.CURRENT_BONUS_PJ_NAMES_RANGE,
        )

    def get_users(self) -> tuple[User, ...]:
        worksheet: Worksheet = self._reader.worksheet(self._user_list_name)
        names: list[Cell] = worksheet.range(self._user_name_range)
        ids: list[Cell] = worksheet.range(self._user_tid_range)
        return tuple(
            User(telegram_id=tid.value, name=name.value)
            for name, tid in zip(names, ids, strict=False)
            if name.value and tid.value
        )

    def get_user_by_tid(self, tid: str) -> User:
        users: tuple[User, ...] = self.get_users()
        user: User | None = next(
            (user for user in users if user.telegram_id.strip() == tid.strip()),
            None,
        )
        if user is None:
            logger.error(f"User with {tid!r} not found")
            raise SheetUserNotFoundError(f"User with {tid!r} not found")
        return user

    def get_bonuses(self) -> tuple[Bonus, ...]:
        worksheet: Worksheet = self._reader.worksheet(self._current_list_name)
        names: list[Cell] = worksheet.range(name=self._current_names_range)
        kpis: list[Cell] = worksheet.range(name=self._current_kpi_range)
        bonuses: list[Cell] = worksheet.range(name=self._current_bonus_range)
        return tuple(
            Bonus(username=name.value, amount=bonus.value, kpi=kpi.value, column_index=name.col)
            for name, bonus, kpi in zip(names, bonuses, kpis, strict=False)
            if name.value and bonus.value and kpi.value
        )

    def get_bonus_by_tid(self, tid: str) -> Bonus:
        user: User = self.get_user_by_tid(tid=tid)
        bonus: Bonus | None = next(
            (bonus for bonus in self.get_bonuses() if bonus.username.strip() == user.name.strip()),
            None,
        )
        if bonus is None:
            logger.error(f"Bonus for {user.name!r} not found")
            raise SheetBonusNotFoundError(f"Bonus for {user.name!r} not found")
        return bonus

    def inject_bonus_projects(self, bonus: Bonus) -> None:
        worksheet: Worksheet = self._reader.worksheet(self._current_list_name)
        names: list[Cell] = worksheet.range(name=self._current_bonus_pj_names_range)
        cell_name: str = rowcol_to_a1(
            row=self._current_bonus_pj_start_row + 1,
            col=bonus.column_index,
        )
        col_name: str = rowcol_to_a1(row=1, col=bonus.column_index)[0:-1]

        bonuses: list[Cell] = worksheet.range(name=f"{cell_name}:{col_name}")
        bonus.bonuses = [
            BonusProject(name=name.value, bonus=bonus.value)
            for name, bonus in zip(names, bonuses, strict=False)
            if name.value and bonus.value
        ]
