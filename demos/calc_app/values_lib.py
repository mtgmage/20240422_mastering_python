import opperations_lib


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


def current_value(pa_opperation_history: dict) -> float:
    ln_value = 0.0
    for ln_id in pa_opperation_history.keys():
        ln_value = opperations_lib.la_math_operations[pa_opperation_history[ln_id]["command"]](ln_value, pa_opperation_history[ln_id]["delta_value"])

    return ln_value
