from typing import Any


def main() -> None:
    lc_var: Any = "Text"
    print(type(lc_var))

    lc_var = 42
    print(type(lc_var))

if __name__ == "__main__":
    main()
