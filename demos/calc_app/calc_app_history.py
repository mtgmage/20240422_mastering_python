def store_opperation(pc_command: str, pn_delta: float, pa_opperations: dict) -> None:
    if len(pa_opperations) > 0:
        ln_id = max(pa_opperations.keys()) + 1
    else:
        ln_id = 1

    match pc_command:
        case "+":
            pc_command = "add"
        case "-":
            pc_command = "subtract"
        case "*":
            pc_command = "multiply"
        case "/":
            pc_command = "divide"

    pa_opperations[ln_id] = {"command": pc_command, "delta_value": pn_delta}


def get_delta() -> float | None:
    lc_delta = input("Enter the delta value: ")

    try:
        ln_delta = float(lc_delta)
    except:
        print("Invalid delta value provided!")
        ln_delta = None

    return ln_delta


def update_value(pc_command: str, pn_value: float, pn_delta: float) -> float | None:
    ln_value = None
    match pc_command:
        case "add" | "+":
            ln_value = pn_value + pn_delta
        case "subtract" | "-":
            ln_value = pn_value - pn_delta
        case "multiply" | "*":
            ln_value = pn_value * pn_delta
        case "divide" | "/":
            if pn_delta == 0:
                print("Cannot divide by 0!")
            else:
                ln_value = pn_value / pn_delta

    return ln_value


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


def main() -> None:
    ln_value: float = 0.0
    la_opperations: dict = {}

    for ln_loop in range(0, 999):
        print(" ")
        print("****************************************")
        print("The current value is: " + str(ln_value))
        print("****************************************")
        print(" ")
        print("Here are the valid commands:")
        print("add (+)")
        print("subtract (-)")
        print("multiply (*)")
        print("divide (/)")
        print("clear (c) - to reset current value to zero")
        print("history (h) - to show the previous commands")
        print("remove (r) - to remove a command from the history")
        print("exit (x) - to terminate")
        lc_command = input("Enter a command: ")
        lc_command = lc_command.lower()

        match lc_command:
            case "exit" | "x":
                print(" ")
                print("Bye :)")
                print(" ")
                break

            case "add" | "+" | "subtract" | "-" | "multiply" | "*" | "divide" | "/":
                ln_delta = get_delta()
                if ln_delta == None:
                    continue

                ln_value = update_value(lc_command, ln_value, ln_delta)
                if ln_value == None:
                    continue

                store_opperation(lc_command, ln_delta, la_opperations)

            case "clear" | "c":
                ln_value = 0
                la_opperations = {}

            case "history" | "h":
                print(" ")
                print("Opperation history:")
                if len(la_opperations) > 0:
                    for ln_id in la_opperations.keys():
                        print(str(ln_id) + " " + la_opperations[ln_id]["command"] + " " + str(la_opperations[ln_id]["delta_value"]))
                else:
                    print("None")

            case "remove" | "r":
                la_opperations = remove_command(la_opperations)


            case _:
                print("Invalid command provided!")


if __name__ == "__main__":
    main()
