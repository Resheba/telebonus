from functools import cache

from pydantic import ValidationInfo, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    # Telegram
    TELEGRAM_TOKEN: str = ""

    TELEGRAM_ME_COMMAND: str = "me"
    TELEGRAM_COMMON_COMMAND: str = "common"

    # Sheet
    SERVICE_ACCOUNT_PATH: str = "./config/cred.json"
    SHEET_KEY: str = ""

    LIST_USERS: str = ""
    USER_NAME_RANGE: str = "A:A"
    USER_TID_RANGE: str = "B:B"

    LIST_CURRENT: str = ""
    CURRENT_BONUS_RANGE: str = "I1:1"
    CURRENT_KPI_RANGE: str = "I2:2"
    CURRENT_NAMES_RANGE: str = "I4:4"

    @field_validator("SHEET_KEY", "LIST_USERS", "LIST_CURRENT", "TELEGRAM_TOKEN")
    @classmethod
    def validate_env(cls, v: str, info: ValidationInfo) -> str:
        if not v:
            raise ValueError(f"{info.field_name} is required")
        return v

    @classmethod
    @cache
    def get_settings(cls) -> "Settings":
        return cls()
