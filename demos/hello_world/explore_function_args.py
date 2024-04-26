def add(pn_num1: float, pn_num2: float) -> float:
    return pn_num1 + pn_num2

print(add(1, 2))

def bigger_function(a, b, *c) -> None:
    print(a, b, c)


def bigger_function2(a, b, *args, **kwargs) -> None:
    print(a, b, args, kwargs)


bigger_function(1,2,3,4)

bigger_function2(1, 2, 3, 4, 5, e=6, f=7)

person = {"name": "Rick", "age": 99}
person2 = {**person, "city": "Redlands"}
print(person)
print(person2)
