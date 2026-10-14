def add_entry(filename, date, entry):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{date}: {entry}\n")

    print("Entry saved successfully.")


def view_entries(filename, date):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith(f"{date}:"):
                    print(line.strip())

    except FileNotFoundError:
        print("Diary file not found.")