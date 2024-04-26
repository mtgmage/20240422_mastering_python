import os
import json
from typing import Protocol
import logging
from pathlib import Path
from main_lib import MathTransaction, Calculator
from data_lib import OpperationHistoryEphemeral, OpperationHistoryDisk


class AppSettings:
    config_file_path: Path = Path("config.json")
    log_file_path: Path = Path("calc_app.log")
    log_level: int = 0
    command_log_file_path: Path = Path("command.log")

    def command_line_args(self) -> None:
        lc_config_file_path = Path("config.json")

        from argparse import ArgumentParser

        lo_parser = ArgumentParser(description="Weird Calculator")
        lo_parser.add_argument("--configfile", "-c", help="Configuration file.", default="config.json")

        lo_args = lo_parser.parse_args()
        if lo_args.configfile and os.path.isfile(lo_args.configfile):
            lc_config_file_path = Path(lo_args.configfile)

        self.config_file_path = lc_config_file_path

    def load_app_configuration(self) -> None:
        lo_level = logging.ERROR
        lc_command_log_file_path = Path("command.log")

        try:
            lc_config_file_path = self.config_file_path

            with lc_config_file_path.open("r", encoding="UTF-8") as lo_config_file:
                la_config_data = json.load(lo_config_file)
                print(la_config_data)

                if la_config_data["logging_filename"] and os.path.isfile(la_config_data["logging_filename"]):
                    self.config_file_path = Path(la_config_data["logging_filename"])

                if la_config_data["logging_level"] == "INFO":
                    lo_level = logging.INFO
                elif la_config_data["logging_level"] == "DEBUG":
                    lo_level = logging.DEBUG

        except IOError as exc:
            print(f"Error: {exc}")

        self.log_level = lo_level
        self.command_log_file_path = lc_command_log_file_path

    def config_logging(self) -> None:
        logging.basicConfig(
            filename=self.log_file_path,
            level=self.log_level,
            format="%(levelname)s: %(message)s",
        )


def main() -> None:
    #lo_opperation_history = OpperationHistoryEphemeral()
    lo_opperation_history = OpperationHistoryDisk()
    lo_transaction = MathTransaction(lo_opperation_history)
    lo_calculator = Calculator()
    lo_settings = AppSettings()
    lo_settings.command_line_args()
    lo_settings.load_app_configuration()
    lo_settings.config_logging()
    lo_calculator.run(lo_transaction)


if __name__ == "__main__":
    main()
