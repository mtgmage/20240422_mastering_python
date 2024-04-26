my_var = "Hello, World!"

def func1() -> None:
    my_var = "The best!"
    print(f"Func1: {my_var}")

    def func2() -> None:
        nonlocal my_var
        my_var = "Mapping is awesome!"
        print(f"Func2: {my_var}")

    func2()

func1()
print(f"Module: {my_var}")
