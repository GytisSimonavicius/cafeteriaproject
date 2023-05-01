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
        self.tables: List[Table] = []

    def add_table(self, table_number: int, capacity: int) -> None:
        new_table: Table = Table(table_number, capacity)
        self.tables.append(new_table)

    def reserve_table(self, name: str, table_number: int) -> None:
        table: Optional[Table] = self.get_table(table_number)
        if table and not table.is_reserved():
            table.reserve(name, datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        else:
            print("Table is already reserved or does not exist.")

    def get_table(self, table_number: int) -> Optional[Table]:
        for table in self.tables:
            if table.table_number == table_number:
                return table
        return None

    def show_tables(self) -> None:
        for table in self.tables:
            status: str = "Free" if not table.is_reserved() else "Reserved"
            print(f"Table {table.table_number} ({table.capacity}-seater): {status}")

    def show_reservation(self, table_number: int) -> None:
        table: Optional[Table] = self.get_table(table_number)
        if table:
            print(f"Table {table.table_number}: {table.reservation_info()}")
        else:
            print("Table not found.")

def main() -> None:
    restaurant: Restaurant = Restaurant("Viva Radvegas Cantina & Grill")
    restaurant.add_table(1, 1)
    restaurant.add_table(2, 1)
    restaurant.add_table(3, 1)
    restaurant.add_table(4, 2)
    restaurant.add_table(5, 2)
    restaurant.add_table(6, 2)
    restaurant.add_table(7, 2)
    restaurant.add_table(8, 4)
    restaurant.add_table(9, 4)
    restaurant.add_table(10, 4)


    while True:
        print("\nOptions:")
        print("1. Reserve a table")
        print("2. Show all tables")
        print("3. Show reservation details")
        print("4. Quit")

        choice: str = input("Enter your choice: ")

        if choice == "1":
            name: str = input("Enter your full name: ")
            table_number: int = int(input("Enter table number: "))
            restaurant.reserve_table(name, table_number)
        elif choice == "2":
            restaurant.show_tables()
        elif choice == "3":
            table_number: int = int(input("Enter table number: "))
            restaurant.show_reservation(table_number)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()