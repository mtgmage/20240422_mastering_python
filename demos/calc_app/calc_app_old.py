def main() -> None:
    ln_value = 0

    for ln_loop in range(0, 999):
        print(" ")
        print("****************************************")
        print("The current value is: " + str(ln_value))
        print("****************************************")
        print(" ")
        print("Here are the valid commands:")
        print("add")
        print("subtract")
        print("multiply")
        print("divide")
        print("clear (to reset current value to zero)")
        print("exit (to terminate)")
        lc_command = input("Enter a command: ")
        lc_command = lc_command.lower()

        match lc_command:
            case "exit":
                print("Bye :)")
                break

            case "clear":
                ln_value = 0

            case "add" | "subtract" | "multiply" | "divide":
                lc_delta = input("Enter the delta value: ")

                try:
                    if "." in lc_delta:
                        ln_delta = float(lc_delta)
                    else:
                        ln_delta = int(lc_delta)
                except:
                    print("Invalid delta value provided!")
                    continue

                match lc_command:
                    case "add":
                        ln_value = ln_value + ln_delta
                    case "subtract":
                        ln_value = ln_value - ln_delta
                    case "multiply":
                        ln_value = ln_value * ln_delta
                    case "divide":
                        if ln_delta == 0:
                            print("Cannot divide by 0!")
                        else:
                            ln_value = ln_value / ln_delta

            case _:
                print("Invalid command provided!")


if __name__ == "__main__":
    main()
