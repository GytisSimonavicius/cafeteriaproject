from typing import Dict, List, Optional
from datetime import datetime
from table import Table

class Restaurant:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.tables: Dict[str, List[Table]] = {
            "single": [Table(table+1, 1) for table in range(10)],
            "double": [Table(table+11, 2) for table in range(10)],
            "family": [Table(table+21, 4) for table in range(5)],
            "group": [Table(table+26, 8) for table in range(2)]
        }

    def reserve_table(self, name: str, reservation_time: datetime, table_number: int) -> None:
        table: Optional[Table] = self.get_table(table_number)
        if table and not table.is_reserved():
            result = table.reserve(name, reservation_time)
            return result
        else:
            return "Table is already reserved or does not exist."

    def get_table(self, table_number: int) -> Optional[Table]:
        for table_list in self.tables.values():
            for table in table_list:
                if table.table_number == table_number:
                    return table
        return None

    def show_tables(self) -> None:
        tables_info = []
        for table_type, table_list in self.tables.items():
            for table in table_list:
                status: str = "Free" if not table.is_reserved() else "Reserved"
                tables_info.append(f"{table_type.capitalize()} table {table.table_number} ({table.capacity} seats): {status}")
        return tables_info

    def show_reservation(self) -> str:
        message = "Would you like to check the reservation by:\n1. Table ID\n2. Customer surname\n"
        
        choice: str = input("Enter your choice: ")
        
        if choice == "1":
            table_number: int = int(input("Enter table ID number: "))
            table: Optional[Table] = self.get_table(table_number)
            if table:
                message += f"Table {table.table_number}: {table.reservation_info()}\n"
            else:
                message += "Table not found.\n"
        elif choice == "2":
            surname: str = input("Enter customer surname: ")
            found_reservation: bool = False
            for table_list in self.tables.values():
                for table in table_list:
                    if table.reservation and table.reservation['name'].split()[1] == surname:
                        message += f"Table {table.table_number}: {table.reservation_info()}\n"
                        found_reservation = True
            if not found_reservation:
                message += "Reservation not found.\n"
        else:
            message += "Invalid choice. Please try again.\n"
        
        return message

    def suggest_table(self, group_size: int) -> str:
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
            return f"Sorry, we don't have any {table_type} tables available for your group.\n"
        else:
            return f"We suggest {table_type} tables for your group of {group_size} people: {free_tables}\nWrite ID number of the {table_type} type table, which you would love to choose.\n"

if __name__ == "__main__":
    pass