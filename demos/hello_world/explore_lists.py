la_nums = [0, 2, 4, 6]
print(" ")
for ln_num in la_nums:
    print(ln_num)

la_letters = ["a", "b", "c", "d"]
print(" ")
for lc_letter in la_letters:
    print(lc_letter)

la_letters.append("e")
print(" ")
for lc_letter in la_letters:
    print(lc_letter)

la_person = {"first_name": "Rick", "last_name": "Wood", "age": 99}

la_people = [
    {"name": "Rick", "age": 99},
    {"name": "Victoria", "age": 12},
    {"name": "Nich", "age": 5},
    ]

print(" ")
for la_person in la_people:
    print(la_person["name"])
    print(la_person["age"])
