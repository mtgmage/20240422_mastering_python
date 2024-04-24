import values_lib


class MathTransaction:
    opperation_history: dict = {}

    def __init__(self) -> None:
        pass

    def next_id(self) -> int:
      if len(self.opperation_history) > 0:
          ln_id = max(self.opperation_history.keys()) + 1
      else:
          ln_id = 1

      return ln_id

    def store_opperation(self, pc_command: str, pn_delta: float) -> None:
      ln_id = self.next_id()
      self.opperation_history[ln_id] = {"command": pc_command, "delta_value": pn_delta}

    def remove_opperation(self) -> None:
      lc_rem_id = input("Enter the command history entry to delete: ")
      try:
          ln_rem_id = int(lc_rem_id)
          if ln_rem_id < 1 or ln_rem_id > max(self.opperation_history.keys()):
              lc_rem_id = ""
      except:
          lc_rem_id = ""

      if not lc_rem_id:
          print("Invalid value provided!")
      else:
          del self.opperation_history[ln_rem_id]

    def display_history(self) -> None:
        print(" ")
        print("Opperation history:")
        if len(self.opperation_history) > 0:
            for ln_id in self.opperation_history.keys():
                print(str(ln_id) + " " + self.opperation_history[ln_id]["command"] + " " + str(self.opperation_history[ln_id]["delta_value"]))
        else:
            print("None")

    def current_value(self) -> float:
      ln_value = 0.0
      for ln_id in self.opperation_history.keys():
          ln_value = values_lib.math_operations[self.opperation_history[ln_id]["command"]](ln_value, self.opperation_history[ln_id]["delta_value"])

      return ln_value

    def clear(self) -> None:
        self.opperation_history = {}


class Calculator():
    hotkeys = {
        "+": "add",
        "-": "subtract",
        "*": "multiply",
        "/": "divide",
        "c": "clear",
        "h": "history",
        "r": "remove",
        "x": "exit",
        }

    def __init__(self) -> None:
        pass

    def run(self, po_transaction: MathTransaction) -> None:
        for ln_loop in range(0, 999):
            print(" ")
            print("****************************************")
            print("The current value is: " + str(po_transaction.current_value()))
            print("****************************************")
            print(" ")
            print("Here are the valid commands:")
            print("add (+) | subtract (-) | multiply (*) | divide (/)")
            print("clear (c) - to reset current value to zero")
            print("history (h) - to show the previous commands")
            print("remove (r) - to remove a command from the history")
            print("exit (x) - to terminate")
            print(" ")
            lc_command = input("Enter a command: ")
            lc_command = lc_command.lower()
            lc_command = self.hotkeys.get(lc_command, lc_command)

            if lc_command in values_lib.math_operations:
                ln_delta = values_lib.get_delta(lc_command)
                if (ln_delta == None):
                    continue

                po_transaction.store_opperation(lc_command, ln_delta)

            elif lc_command == "clear":
                po_transaction.clear()

            elif lc_command == "history":
                po_transaction.display_history()

            elif lc_command == "remove":
                po_transaction.remove_opperation()

            elif lc_command == "exit":
                print(" ")
                print("Bye :)")
                print(" ")
                break

            else:
                print("Invalid command provided!")
