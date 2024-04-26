import json


class Person:
     def __init__(self, name: str, age: int, city: str):
         self.name = name
         self.age = age
         self.city = city


def main() -> None:
    la_people_dict = []
    la_people_dict.append({"name": "Rick W", "age": 99, "city": "Redlands"})
    la_people_dict.append({"name": "Victoria B", "age": 12, "city": "Riverside"})
    la_people_dict.append({"name": "Tsunoda", "age": 5, "city": "Dumpster"})

    la_people_obj = []
    la_people_obj.append(Person("Rick W", 99, "Redlands"))
    la_people_obj.append(Person("Victoria B", 12, "Riverside"))
    la_people_obj.append(Person("Tsunoda", 5, "Dumpster"))

    print(la_people_obj)
    la_people_dict2 = [p.__dict__ for p in la_people_obj]
    print(la_people_dict2)

    with open("data.json", "w") as lo_file:
        json.dump(la_people_dict2, lo_file)
        #lo_file.write("Hello, World!")

    with open("data.json", "r") as lo_file:
        la_people_dict3 = json.load(lo_file)
        print(" ")
        for la_person in la_people_dict3:
            print(la_person)

        la_people_obj2 = [Person(p["name"], p["age"], p["city"]) for p in la_people_dict3]
        print(la_people_obj2)
        #print(lo_file.readlines())


if __name__ == "__main__":
    main()
