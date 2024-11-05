from src.core import BaseAppError


class SheetError(BaseAppError): ...


class SheetNotFoundError(SheetError):
    message: str = "Sheet not found"
