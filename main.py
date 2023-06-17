from restaurant import Restaurant
from datetime import datetime

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
            print(restaurant.suggest_table(group_size))
            table_number: int = int(input("Enter table number: "))
            full_name: str = f"{first_name} {last_name}"
            reservation_time = datetime.strptime(input('What time would you like to reserve a table? Please provide the date and time in the format YYYY-MM-DD HH:MM: '), "%Y-%m-%d %H:%M")
            print(restaurant.reserve_table(full_name, reservation_time, table_number))
        elif choice == "2":
            tables = restaurant.show_tables()
            for table in tables:
                print(table)
        elif choice == "3":
            print(restaurant.show_reservation())
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
