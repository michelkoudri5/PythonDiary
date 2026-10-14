from diary import add_entry, view_entries


def main():
    filename = input("Enter diary filename: ")

    while True:
        print("\n1. Add diary entry")
        print("2. View entries by date")
        print("3. Change diary file")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            entry = input("Enter diary entry: ")
            add_entry(filename, date, entry)

        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            view_entries(filename, date)

        elif choice == "3":
            filename = input("Enter another diary filename: ")

        elif choice == "4":
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()