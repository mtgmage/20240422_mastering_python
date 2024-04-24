class Person:
    def __init__(self, pc_first_name: str, pc_last_name: str, pn_age: int, pc_city: str) -> None:
        self.first_name = pc_first_name
        self.last_name = pc_last_name
        self.age = pn_age
        self.city = pc_city

    def full_name(self) -> str:
        lc_full_name = self.first_name + " " + self.last_name
        return lc_full_name


def full_name(la_person: dict) -> None:
    print(la_person["first_name"] + " " + la_person["last_name"])


la_person1 = {"first_name": "Rick", "last_name": "Wood", "age": 48, "city": "Redlands"}
full_name(la_person1)

la_person2 = Person("Rick", "Wood", 48, "Redlands")
print(la_person2.full_name())

la_person3 = Person("Victoria", "Boehme", 31, "Redlands")
print(la_person3.full_name())
