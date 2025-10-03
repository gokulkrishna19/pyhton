# hotel_management.py
# Simple Hotel Management System (console-based)

class Hotel:
    def __init__(self, name, total_rooms):
        self.name = name
        self.total_rooms = total_rooms
        self.available_rooms = total_rooms
        self.guests = {}  # room_number -> guest_name

    def check_in(self, guest_name):
        if self.available_rooms > 0:
            room_number = self.total_rooms - self.available_rooms + 1
            self.guests[room_number] = guest_name
            self.available_rooms -= 1
            print(f"✅ {guest_name} checked in. Room No: {room_number}")
        else:
            print("⚠️ No rooms available!")

    def check_out(self, room_number):
        if room_number in self.guests:
            guest = self.guests.pop(room_number)
            self.available_rooms += 1
            print(f"👋 {guest} checked out. Room No: {room_number} is now available.")
        else:
            print("⚠️ Invalid room number or room not occupied.")

    def display_status(self):
        print("\n=== Hotel Status ===")
        print(f"Hotel Name: {self.name}")
        print(f"Total Rooms: {self.total_rooms}")
        print(f"Available Rooms: {self.available_rooms}")
        print("Occupied Rooms:")
        if self.guests:
            for room, guest in self.guests.items():
                print(f"  Room {room}: {guest}")
        else:
            print("  None")
        print("====================\n")


def main():
    hotel = Hotel("Grand Python Hotel", 5)

    while True:
        print("\n=== Hotel Management Menu ===")
        print("1. Check-in")
        print("2. Check-out")
        print("3. Display Status")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter guest name: ")
            hotel.check_in(name)

        elif choice == "2":
            try:
                room_no = int(input("Enter room number: "))
                hotel.check_out(room_no)
            except ValueError:
                print("⚠️ Invalid room number.")

        elif choice == "3":
            hotel.display_status()

        elif choice == "4":
            print("👋 Exiting Hotel Management System...")
            break

        else:
            print("⚠️ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
