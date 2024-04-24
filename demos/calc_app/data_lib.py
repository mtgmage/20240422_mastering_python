from typing import Protocol


class OpperationHistory(Protocol):
    def get_history(self) -> list[tuple[int, str, float]]: ...

    def put_history(self) -> bool: ...
