import os
import csv
import json
import logging
from pathlib import Path
import values_lib
from data_lib import OpperationHistory


class MathTransaction:
    def __init__(self, po_opperation_history: OpperationHistory) -> None:
        self.opperation_history = po_opperation_history

    def next_id(self) -> str:
      la_opperation_history = self.opperation_history.get_history()
      if len(la_opperation_history) > 0:
          lc_id = str(int(max(la_opperation_history.keys())) + 1)
      else:
          lc_id = "1"

      return lc_id

    def store_opperation(self, pc_command: str, pn_delta: float) -> None:
      ln_id = self.next_id()
      la_opperation_history = self.opperation_history.get_history()
      la_opperation_history[ln_id] = {"command": pc_command, "delta_value": pn_delta}
      self.opperation_history.put_history(la_opperation_history)

    def remove_opperation(self) -> None:
      la_opperation_history = self.opperation_history.get_history()
      lc_rem_id = input("Enter the command history entry to delete: ")
      if lc_rem_id not in la_opperation_history.keys():
          lc_rem_id = ""

      if not lc_rem_id:
          logging.error("Invalid value provided!")
          #print("Invalid value provided!")
      else:
          del la_opperation_history[lc_rem_id]
          self.opperation_history.put_history(la_opperation_history)

    def display_history(self) -> None:
        la_opperation_history = self.opperation_history.get_history()
        print(" ")
        print("Opperation history:")
        if len(la_opperation_history) > 0:
            for lc_id in la_opperation_history.keys():
                print(lc_id + " " + la_opperation_history[lc_id]["command"] + " " + str(la_opperation_history[lc_id]["delta_value"]))
        else:
            print("None")

    def save_history(self) -> None:
        la_opperation_history = self.opperation_history.get_history()
        lc_file = input("Enter the filename to save command history: ")
        lc_file_type = os.path.splitext(lc_file)[1]
        lc_file_type = lc_file_type.replace(".", "").upper()
        lo_file_path = Path(lc_file)

        if lc_file_type == "CSV":
            la_field_names = ["id", "command", "delta_value"]
            with lo_file_path.open("w", encoding="UTF-8") as lo_file:
                csv_writer = csv.DictWriter(lo_file, fieldnames=la_field_names, delimiter=",")
                csv_writer.writeheader()

                for lc_id in la_opperation_history:
                    csv_writer.writerow({"id": lc_id, "command": la_opperation_history[lc_id]["command"], "delta_value": la_opperation_history[lc_id]["delta_value"]})

        elif lc_file_type == "JSON":
            with lo_file_path.open("w", encoding="UTF-8") as lo_file:
                        json.dump(la_opperation_history, lo_file)

        else:
            logging.error("Invalid file provided!  Supported file types are CSV and JSON.")

    def load_history(self) -> None:
        ll_cont = True
        la_opperation_history = {}
        lc_file = input("Enter the filename to load command history: ")
        if not os.path.isfile(lc_file):
            logging.error("File not found!")
            ll_cont = False

        if ll_cont:
            lc_file_type = os.path.splitext(lc_file)[1]
            lc_file_type = lc_file_type.replace(".", "").upper()
            lo_file_path = Path(lc_file)

            if lc_file_type == "CSV":
                with lo_file_path.open("r", encoding="UTF-8") as lo_file:
                    csv_reader = csv.DictReader(lo_file, delimiter=",")
                    for la_history_row in csv_reader:
                        la_opperation_history[la_history_row["id"]] = {"command": la_history_row["command"], "delta_value": float(la_history_row["delta_value"])}

            elif lc_file_type == "JSON":
                with lo_file_path.open("r", encoding="UTF-8") as lo_file:
                    la_opperation_history = json.load(lo_file)

            else:
                logging.error("Invalid file provided!  Supported file types are CSV and JSON.")
                ll_cont = False

        if ll_cont:
            self.opperation_history.put_history(la_opperation_history)

    def current_value(self) -> float:
      la_opperation_history = self.opperation_history.get_history()
      ln_value = 0.0
      for lc_id in la_opperation_history.keys():
          ln_value = values_lib.math_operations[la_opperation_history[lc_id]["command"]](ln_value, la_opperation_history[lc_id]["delta_value"])

      return ln_value

    def clear(self) -> None:
        self.opperation_history.put_history({})


class Calculator():
    hotkeys = {
        "+": "add",
        "-": "subtract",
        "*": "multiply",
        "/": "divide",
        "c": "clear",
        "h": "history",
        "r": "remove",
        "s": "save",
        "l": "load",
        "x": "exit",
        }

    def __init__(self) -> None:
        pass

    def config_logging(self) -> None:
        try:
            lc_config_file_path = Path("config.json")

            with lc_config_file_path.open("r", encoding="UTF-8") as lo_config_file:
                la_config_data = json.load(lo_config_file)

            if la_config_data["level"] == "INFO":
                lo_level = logging.INFO
            elif la_config_data["level"] == "DEBUG":
                lo_level = logging.DEBUG
            else:
                lo_level = logging.ERROR

            logging.basicConfig(
                filename=la_config_data["filename"],
                level=lo_level,
                format="%(levelname)s: %(message)s",
            )

        except IOError as exc:
            print(f"Error: {exc}")


    def run(self, po_transaction: MathTransaction) -> None:
        for ln_loop in range(0, 999):
            print(" ")
            print("****************************************")
            print("The current value is: " + str(po_transaction.current_value()))
            print("****************************************")
            print(" ")
            print("Here are the valid commands:")
            print("add (+) | subtract (-) | multiply (*) | divide (/)")
            print("clear (c) - clear history and set current value to zero")
            print("history (h) - show the previous commands")
            print("remove (r) - remove a command from the history")
            print("save (s) - save command history to a file")
            print("load (l) - load command history from a file")
            print("exit (x) - to terminate")
            print(" ")
            lc_command = input("Enter a command: ")
            lc_command = lc_command.lower()
            lc_command = self.hotkeys.get(lc_command, lc_command)

            if lc_command in values_lib.math_operations:
                ln_delta = values_lib.get_delta(lc_command)
                if (ln_delta is None):
                    continue

                po_transaction.store_opperation(lc_command, ln_delta)

            elif lc_command == "clear":
                po_transaction.clear()

            elif lc_command == "history":
                po_transaction.display_history()

            elif lc_command == "remove":
                po_transaction.remove_opperation()

            elif lc_command == "save":
                po_transaction.save_history()

            elif lc_command == "load":
                po_transaction.load_history()

            elif lc_command == "exit":
                print(" ")
                print("Bye :)")
                print(" ")
                break

            else:
                logging.error("Invalid command provided!")
                #print("Invalid command provided!")
