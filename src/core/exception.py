class BaseAppError(Exception):
    def __init__(self, message: str | None = None, *args: object) -> None:
        if message:
            self.add_note(message)
        super().__init__(*args)
