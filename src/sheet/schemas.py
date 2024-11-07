class User:
    __slots__ = ("telegram_id", "name")

    def __init__(self, telegram_id: str, name: str) -> None:
        self.telegram_id: str = telegram_id
        self.name: str = name

    def __repr__(self) -> str:
        return f"User({self.telegram_id}, {self.name!r})"


class Bonus:
    __slots__ = ("username", "amount", "kpi", "column_index", "bonuses")

    def __init__(self, username: str, amount: str, kpi: str, column_index: int) -> None:
        self.username: str = username
        self.amount: str = amount
        self.kpi: str = kpi
        self.column_index: int = column_index
        self.bonuses: list[BonusProject] | None = None

    def __repr__(self) -> str:
        return f"Bonus({self.username!r}, {self.amount!r}, {self.kpi!r}, col={self.column_index!r})"


class BonusProject:
    __slots__ = ("name", "bonus")

    def __init__(self, name: str, bonus: str) -> None:
        self.name: str = name
        self.bonus: str = bonus
