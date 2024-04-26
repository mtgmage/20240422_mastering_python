import logging


logging.basicConfig(level = logging.DEBUG)
class CalcAppDivideByZeroError(Exception): ...


def divide(pn_num1: float, pn_num2: float) -> float:
    if pn_num2 == 0:
        raise CalcAppDivideByZeroError("Cannot divide by 0!")
    return pn_num1/pn_num2


def main() -> None:
    logging.debug("This is a debug message")
    logging.info("This is an info message")

    try:
        print(int("k"))
    except ValueError as e:
        logging.error(f"Value Error: {e}")
    except Exception as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    main()
