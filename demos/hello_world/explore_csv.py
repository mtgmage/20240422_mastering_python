from pathlib import Path
import csv


def write_csv() -> None:
    names_file_path = Path("names.csv")
    with names_file_path.open("w", encoding="UTF-8") as lo_file:
        names_csv_writer = csv.writer(lo_file, delimiter=",")
        names_csv_writer.writerow(["first_name", "last_name"])
        names_csv_writer.writerow(["Rick", "Wood"])
        names_csv_writer.writerow(["Victoria", "B"])
        names_csv_writer.writerow(["Willow", "Wood"])

def read_csv() -> None:
    names_file_path = Path("names.csv")
    with names_file_path.open("r", encoding="UTF-8") as lo_file:
        names_csv_reader = csv.reader(lo_file, delimiter=",")
        next(names_csv_reader) # Skip header row
        for name_row in names_csv_reader:
            print(name_row)

def write_csv_dict() -> None:
    names_file_path = Path("names.csv")
    la_field_names = ["first_name", "last_name"]
    with names_file_path.open("w", encoding="UTF-8") as lo_file:
        names_csv_writer = csv.DictWriter(lo_file, fieldnames=la_field_names, delimiter=",")
        names_csv_writer.writeheader()
        names_csv_writer.writerow({"first_name": "Bob", "last_name": "Smith"})
        names_csv_writer.writerow({"first_name": "Rick", "last_name": "W"})

def read_csv_dict() -> None:
    names_file_path = Path("names.csv")
    with names_file_path.open("r", encoding="UTF-8") as lo_file:
        names_csv_reader = csv.DictReader(lo_file, delimiter=",")
        for name_row in names_csv_reader:
            print(name_row)

def main() -> None:
    #write_csv()
    write_csv_dict()
    #read_csv()
    read_csv_dict()


if __name__ == "__main__":
    main()
