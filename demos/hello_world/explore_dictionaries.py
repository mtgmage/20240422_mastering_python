def main() -> None:
    la_person = {"first_name": "Rick", "last_name": "Wood", "age": 99}
    print(la_person["first_name"])
    print(la_person)

    la_person["hair_color"] = "blonde"

    for lc_key in la_person.keys():
        print(la_person[lc_key])

    print(la_person.get("bogus_key", "bogus_value"))
    la_person["bogus_key"] = "real_value"
    print(la_person.get("bogus_key", "bogus_value"))


if __name__ == "__main__":
    main()
