from typing import Callable


la_math_operations: dict[str, Callable[[float, float], float]] = {
    "add": lambda ln_num1, ln_num2: ln_num1 + ln_num2,
    "subtract": lambda ln_num1, ln_num2: ln_num1 - ln_num2,
    "multiply": lambda ln_num1, ln_num2: ln_num1 * ln_num2,
    "divide": lambda ln_num1, ln_num2: ln_num1 / ln_num2,
    }

def store_opperation(pc_command: str, pn_delta: float, pa_opperations: dict) -> None:
    if len(pa_opperations) > 0:
        ln_id = max(pa_opperations.keys()) + 1
    else:
        ln_id = 1

    pa_opperations[ln_id] = {"command": pc_command, "delta_value": pn_delta}


def get_delta(pc_command: str) -> float | None:
    lc_delta = input("Enter the delta value: ")

    try:
        ln_delta = float(lc_delta)
        if pc_command == "divide" and ln_delta == 0:
            print("Cannot divide by 0!")
            ln_delta = None
    except:
        print("Invalid delta value provided!")
        ln_delta = None

    return ln_delta


def remove_command(pa_opperations: dict) -> dict:
    ln_rem_id = input("Enter the command history entry to delete: ")
    try:
        ln_rem_id = int(ln_rem_id)
        if ln_rem_id < 1 or ln_rem_id > max(pa_opperations.keys()):
            ln_rem_id = None
    except:
        ln_rem_id = None

    if ln_rem_id == None:
        print("Invalid value providsed")
    else:
        del pa_opperations[ln_rem_id]

    return pa_opperations


def current_value(pa_opperations: dict) -> float:
    ln_value = 0
    for ln_id in pa_opperations.keys():
        ln_value = la_math_operations[pa_opperations[ln_id]["command"]](ln_value, pa_opperations[ln_id]["delta_value"])

    return ln_value


def main() -> None:
    la_opperations: dict = {}
    la_hotkeys = {
        "+": "add",
        "-": "subtract",
        "*": "multiply",
        "/": "divide",
        "c": "clear",
        "h": "history",
        "r": "remove",
        "x": "exit",
        }

    for ln_loop in range(0, 999):
        print(" ")
        print("****************************************")
        print("The current value is: " + str(current_value(la_opperations)))
        print("****************************************")
        print(" ")
        print("Here are the valid commands:")
        print("add (+), subtract (-), multiply (*), divide (/)")
        print("clear (c) - to reset current value to zero")
        print("history (h) - to show the previous commands")
        print("remove (r) - to remove a command from the history")
        print("exit (x) - to terminate")
        lc_command = input("Enter a command: ")
        lc_command = lc_command.lower()
        lc_command = la_hotkeys.get(lc_command, lc_command)

        if lc_command in la_math_operations:
            ln_delta = get_delta(lc_command)
            if (ln_delta == None):
                continue

            store_opperation(lc_command, ln_delta, la_opperations)

        elif lc_command == "clear":
            la_opperations = {}

        elif lc_command == "history":
            print(" ")
            print("Opperation history:")
            if len(la_opperations) > 0:
                for ln_id in la_opperations.keys():
                    print(str(ln_id) + " " + la_opperations[ln_id]["command"] + " " + str(la_opperations[ln_id]["delta_value"]))
            else:
                print("None")

        elif lc_command == "remove":
            la_opperations = remove_command(la_opperations)

        elif lc_command == "exit":
            print(" ")
            print("Bye :)")
            print(" ")
            break

        else:
            print("Invalid command provided!")


if __name__ == "__main__":
    main()
