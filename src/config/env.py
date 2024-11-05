from pydantic_settings import BaseSettings, SettingsConfigDict


@lambda s: s()
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    SERVICE_ACCOUNT_PATH: str = "./config/cred.json"
    SHEET_KEY: str

    LIST_USERS: str
    USER_NAME_COL: int = 1
    USER_TID_COL: int = 2

    LIST_LATEST: str
