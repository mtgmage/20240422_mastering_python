from main_lib import MathTransaction, Calculator
from data_lib import OpperationHistoryEphemeral, OpperationHistoryDisk


def main() -> None:

    #lo_opperation_history = OpperationHistoryEphemeral()
    lo_opperation_history = OpperationHistoryDisk()
    lo_transaction = MathTransaction(lo_opperation_history)
    lo_calculator = Calculator()
    lo_calculator.config_logging()
    lo_calculator.run(lo_transaction)


if __name__ == "__main__":
    main()
