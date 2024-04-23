import opperations_lib
import values_lib


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
        print("The current value is: " + str(values_lib.current_value(la_opperations)))
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

        if lc_command in opperations_lib.la_math_operations:
            ln_delta = values_lib.get_delta(lc_command)
            if (ln_delta == None):
                continue

            opperations_lib.store_opperation(lc_command, ln_delta, la_opperations)

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
            la_opperations = opperations_lib.remove_opperation(la_opperations)

        elif lc_command == "exit":
            print(" ")
            print("Bye :)")
            print(" ")
            break

        else:
            print("Invalid command provided!")


if __name__ == "__main__":
    main()
