import datetime
from typing import Optional, Dict, List, Union

class Table:
    def __init__(self, table_number: int, capacity: int) -> None:
        self.table_number: int = table_number
        self.capacity: int = capacity
        self.reservation: Optional[Dict[str, Union[str, datetime.datetime]]] = None

    def reserve(self, name: str, time: str) -> None:
        self.reservation = {
            "name": name,
            "time": time
        }
        print(f"Table {self.table_number} reserved for {name} at {time}.")

    def is_reserved(self) -> bool:
        return self.reservation is not None

    def reservation_info(self) -> str:
        if self.reservation:
            return f"Reserved by {self.reservation['name']} at {self.reservation['time']}"
        else:
            return "Not reserved"

class Restaurant:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.tables: Dict[str, List[Table]] = {
            "single": [Table(table+1, 1) for table in range(10)],
            "double": [Table(table+11, 2) for table in range(10)],
            "family": [Table(table+21, 4) for table in range(5)],
            "group": [Table(table+26, 8) for table in range(2)]
        }

    def reserve_table(self, name: str, table_number: int) -> None:
        table: Optional[Table] = self.get_table(table_number)
        if table and not table.is_reserved():
            table.reserve(name, datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        else:
            print("Table is already reserved or does not exist.")

    def get_table(self, table_number: int) -> Optional[Table]:
        for table_list in self.tables.values():
            for table in table_list:
                if table.table_number == table_number:
                    return table
        return None

    def show_tables(self) -> None:
        for table_type, table_list in self.tables.items():
            for table in table_list:
                status: str = "Free" if not table.is_reserved() else "Reserved"
                print(f"{table_type.capitalize()} table {table.table_number} ({table.capacity} seats): {status}")

    def show_reservation(self) -> None:
        print("Would you like to check the reservation by:")
        print("1. Table ID")
        print("2. Customer surname")
        choice: str = input("Enter your choice: ")
        
        if choice == "1":
            table_number: int = int(input("Enter table ID number: "))
            table: Optional[Table] = self.get_table(table_number)
            if table:
                print(f"Table {table.table_number}: {table.reservation_info()}")
            else:
                print("Table not found.")
        elif choice == "2":
            surname: str = input("Enter customer surname: ")
            found_reservation: bool = False
            for table_list in self.tables.values():
                for table in table_list:
                    if table.reservation and table.reservation['name'].split()[1] == surname:
                        print(f"Table {table.table_number}: {table.reservation_info()}")
                        found_reservation = True
            if not found_reservation:
                print("Reservation not found.")
        else:
            print("Invalid choice. Please try again.")


    def suggest_table(self, group_size: int) -> None:
        if group_size == 1:
            table_type = "single"
        elif group_size == 2:
            table_type = "double"
        elif 3 <= group_size <= 4:
            table_type = "family"
        elif group_size >= 5:
            table_type = "group"

        table_list: List[Table] = self.tables[table_type]
        free_tables: List[int] = [table.table_number for table in table_list if not table.is_reserved()]

        if not free_tables:
            print(f"Sorry, we don't have any {table_type} tables available for your group.")
        else:
            print(f"We suggest {table_type} tables for your group of {group_size} people.")
            print(free_tables)
            print(f"Write ID number of the {table_type} type table, which you would love to choose.")


def main() -> None:
    restaurant: Restaurant = Restaurant("Viva Radvegas Cantina & Grill")
    while True:
        print("\nDear Sir/Maddam.What would you like to do?")
        print("1. Reserve a table")
        print("2. Show all tables")
        print("3. Show reservation details")
        print("4. Quit")

        choice: str = input("Enter your choice: ")

        if choice == "1":
            first_name: str = input("Enter your first name: ")
            last_name: str = input("Enter your last name: ")
            group_size: int = int(input("Enter the number of people in your group: "))
            restaurant.suggest_table(group_size)
            table_number: int = int(input("Enter table number: "))
            full_name: str = f"{first_name} {last_name}"
            restaurant.reserve_table(full_name, table_number)
        elif choice == "2":
            restaurant.show_tables()
        elif choice == "3":
            restaurant.show_reservation()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

