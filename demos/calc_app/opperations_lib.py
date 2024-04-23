from typing import Callable


la_math_operations: dict[str, Callable[[float, float], float]] = {
    "add": lambda ln_num1, ln_num2: ln_num1 + ln_num2,
    "subtract": lambda ln_num1, ln_num2: ln_num1 - ln_num2,
    "multiply": lambda ln_num1, ln_num2: ln_num1 * ln_num2,
    "divide": lambda ln_num1, ln_num2: ln_num1 / ln_num2,
    }


def store_opperation(pc_command: str, pn_delta: float, pa_opperation_history: dict) -> None:
    if len(pa_opperation_history) > 0:
        ln_id = max(pa_opperation_history.keys()) + 1
    else:
        ln_id = 1

    pa_opperation_history[ln_id] = {"command": pc_command, "delta_value": pn_delta}


def remove_opperation(pa_opperation_history: dict) -> dict:
    lc_rem_id = input("Enter the command history entry to delete: ")
    try:
        ln_rem_id = int(lc_rem_id)
        if ln_rem_id < 1 or ln_rem_id > max(pa_opperation_history.keys()):
            lc_rem_id = ""
    except:
        lc_rem_id = ""

    if not lc_rem_id:
        print("Invalid value provided!")
    else:
        del pa_opperation_history[ln_rem_id]

    return pa_opperation_history
