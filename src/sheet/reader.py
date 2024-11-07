from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING

from gspread.auth import service_account
from gspread.exceptions import GSpreadException, WorksheetNotFound
from gspread.worksheet import Worksheet
from loguru import logger

from .exception import SheetError, SheetNotFoundError

if TYPE_CHECKING:
    from gspread.client import Client
    from gspread.spreadsheet import Spreadsheet


class Reader:
    __slots__ = ("_client", "_sheet")

    def __init__(self, secret_filename: str | Path, sheet_key: str) -> None:
        self._client: Client = service_account(filename=secret_filename)
        self._sheet: Spreadsheet = self._client.open_by_key(key=sheet_key)

    @lru_cache(maxsize=5)
    def _worksheet(self, worksheet: str) -> Worksheet:
        try:
            return self._sheet.worksheet(worksheet)
        except WorksheetNotFound as ex:
            logger.error(f"Worksheet {worksheet!r} not found")
            raise SheetNotFoundError(f"Worksheet {worksheet!r} not found") from ex
        except GSpreadException as ex:
            logger.error(ex)
            raise SheetError from ex

    def worksheet(self, worksheet: str) -> Worksheet:
        return self._worksheet(worksheet=worksheet)
