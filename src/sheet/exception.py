from src.core import BaseAppError


class SheetError(BaseAppError): ...


class SheetNotFoundError(SheetError):
    message: str = "Sheet not found"


class SheetUserNotFoundError(SheetError):
    message: str = "User not found"


class SheetBonusNotFoundError(SheetError):
    message: str = "Bonus not found"
