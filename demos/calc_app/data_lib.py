import os
import json
from typing import Protocol


class OpperationHistory(Protocol):
    def get_history(self) -> dict[str, dict]: ...

    def put_history(self, pa_opperation_history: dict) -> None: ...


class OpperationHistoryEphemeral:
    opperation_history: dict = {}

    def get_history(self) -> dict:
        return self.opperation_history

    def put_history(self, pa_opperation_history: dict) -> None:
        self.opperation_history = pa_opperation_history


class OpperationHistoryDisk:
    def get_history(self) -> dict:
        la_opperation_history = {}
        if os.path.isfile("opperation_history_data.json"):
            with open("opperation_history_data.json", "r") as lo_file:
                la_opperation_history = json.load(lo_file)

        return la_opperation_history

    def put_history(self, pa_opperation_history: dict) -> None:
        with open("opperation_history_data.json", "w") as file:
            json.dump(pa_opperation_history, file)
