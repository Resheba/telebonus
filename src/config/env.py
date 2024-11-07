from functools import cache
from typing import Self

from gspread.utils import a1_range_to_grid_range
from pydantic import ValidationInfo, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    # Telegram
    TELEGRAM_TOKEN: str = ""

    TELEGRAM_ME_COMMAND: str = "me"

    # Sheet
    SERVICE_ACCOUNT_PATH: str = "./config/cred.json"
    SHEET_KEY: str = ""

    LIST_USERS: str = "users"
    USER_NAME_RANGE: str = "A:A"
    USER_TID_RANGE: str = "B:B"

    LIST_CURRENT: str = "current_bonus"
    CURRENT_BONUS_RANGE: str = "I1:1"
    CURRENT_KPI_RANGE: str = "I2:2"
    CURRENT_NAMES_RANGE: str = "I4:4"

    CURRENT_BONUS_PJ_NAMES_RANGE: str = "B5:B"

    @field_validator("SHEET_KEY", "LIST_USERS", "LIST_CURRENT", "TELEGRAM_TOKEN")
    @classmethod
    def validate_env(cls, v: str, info: ValidationInfo) -> str:
        if not v:
            raise ValueError(f"{info.field_name} is required")
        return v

    @field_validator("CURRENT_BONUS_PJ_NAMES_RANGE")
    @classmethod
    def validate_pj_start_row(cls, v: str, info: ValidationInfo) -> str:
        if not v:
            raise ValueError(f"{info.field_name} is required")
        if a1_range_to_grid_range(v).get("startRowIndex") is None:
            raise ValueError(f"{info.field_name} is invalid, row index is required")
        return v

    @classmethod
    @cache
    def get_settings(cls) -> Self:
        return cls()
