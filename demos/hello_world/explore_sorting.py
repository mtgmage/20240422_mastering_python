from random import randint

# -- Inherent sort order
la_nums = [randint(0,10) for _ in range(9)]
print(la_nums)
print(sorted(la_nums))
print(la_nums)

la_nums.sort()
print(la_nums)

class Food:
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country

    def __str__(self) -> str:
        return f"name: {self.name}, country: {self.country}"


foods = [
    Food("steak", "USA"),
    Food("kuba", "Iraq"),
    Food("crabcakes", "England"),
    Food("sushi", "Japan"),
    Food("toad in the hole", "England"),
    Food("peking duck", "China"),
]

print(list(str(f) for f in sorted(foods, key=lambda x: x.name)))
