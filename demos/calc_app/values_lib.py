from typing import Callable


math_operations: dict[str, Callable[[float, float], float]] = {
    "add": lambda ln_num1, ln_num2: ln_num1 + ln_num2,
    "subtract": lambda ln_num1, ln_num2: ln_num1 - ln_num2,
    "multiply": lambda ln_num1, ln_num2: ln_num1 * ln_num2,
    "divide": lambda ln_num1, ln_num2: ln_num1 / ln_num2,
    }


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
