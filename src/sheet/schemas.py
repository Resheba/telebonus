class User:
    __slots__ = ("telegram_id", "name")

    def __init__(self, telegram_id: str, name: str) -> None:
        self.telegram_id: str = telegram_id
        self.name: str = name

    def __repr__(self) -> str:
        return f"User({self.telegram_id}, {self.name!r})"
