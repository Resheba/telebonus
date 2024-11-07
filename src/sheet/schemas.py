class User:
    __slots__ = ("telegram_id", "name")

    def __init__(self, telegram_id: str, name: str) -> None:
        self.telegram_id: str = telegram_id
        self.name: str = name

    def __repr__(self) -> str:
        return f"User({self.telegram_id}, {self.name!r})"


class Bonus:
    __slots__ = ("username", "amount", "kpi")

    def __init__(self, username: str, amount: str, kpi: str) -> None:
        self.username: str = username
        self.amount: str = amount
        self.kpi: str = kpi

    def __repr__(self) -> str:
        return f"Bonus({self.username!r}, {self.amount!r}, {self.kpi!r})"
