from typing import Optional, Dict, Union
import datetime

class Table:
    def __init__(self, table_number: int, capacity: int) -> None:
        self.table_number: int = table_number
        self.capacity: int = capacity
        self.reservation: Optional[Dict[str, Union[str, datetime.datetime, datetime.datetime]]] = None

    def reserve(self, name: str, reservation_time: datetime.datetime) -> str:
        self.reservation = {
            "name": name,
            "reservation_time": reservation_time, 
        }
        return f"Table {self.table_number} reserved for {name} at {reservation_time}."

    def is_reserved(self) -> bool:
        return self.reservation is not None

    def reservation_info(self) -> str:
        if self.reservation:
            return f"Reserved by {self.reservation['name']} at {self.reservation['reservation_time']}"
        else:
            return "Not reserved"
    
if __name__ == "__main__":
    # raise RuntimeError("You cannot run this directly")
    pass