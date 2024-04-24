import main_lib


def main() -> None:
    lo_transaction = main_lib.MathTransaction()
    lo_calculator = main_lib.Calculator()
    lo_calculator.run(lo_transaction)


if __name__ == "__main__":
    main()
