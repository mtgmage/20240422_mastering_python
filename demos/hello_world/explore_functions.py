def num_input(pc_prompt: str ="Enter another number: ") -> int:
    lc_retval = input(pc_prompt)
    try:
        ln_retval = int(lc_retval)
    except:
        ln_retval = 0

    return ln_retval


def sum_values(pn_val1: int, pn_val2: int) -> int:
    ln_total = pn_val1 + pn_val2

    return ln_total


def main() -> None:
    ln_num1 = num_input("Enter a number: ")
    ln_num2 = num_input()
    ln_num3 = num_input()

    ln_total = sum_values(ln_num1, ln_num2)
    ln_total = sum_values(ln_total, ln_num3)
    print(ln_total)

if __name__ == "__main__":
    main()
