# transport_booking.py
# Demonstrates Polymorphism with a Transport Booking System

class Transport:
    def book_ticket(self):
        raise NotImplementedError("Subclass must implement this method")


class Bus(Transport):
    def book_ticket(self):
        name = input("🧍 Enter passenger name: ")
        seats = int(input("Enter number of seats: "))
        print(f"🚌 Bus ticket booked for {name} ({seats} seat(s)).\n")
        return f"Bus Booking → {name}, Seats: {seats}"


class Train(Transport):
    def book_ticket(self):
        name = input("🧍 Enter passenger name: ")
        seats = int(input("Enter number of seats: "))
        print(f"🚆 Train ticket booked for {name} ({seats} seat(s)).\n")
        return f"Train Booking → {name}, Seats: {seats}"


class Flight(Transport):
    def book_ticket(self):
        name = input("🧍 Enter passenger name: ")
        seats = int(input("Enter number of seats: "))
        print(f"✈️ Flight ticket booked for {name} ({seats} seat(s)).\n")
        return f"Flight Booking → {name}, Seats: {seats}"


# Polymorphic function
def process_booking(transport_type):
    return transport_type.book_ticket()


# -------- Main Program --------
if __name__ == "__main__":
    print("===== ✈️ Transport Booking System =====")

    bookings = []
    while True:
        print("\n1. Bus Booking")
        print("2. Train Booking")
        print("3. Flight Booking")
        print("4. Show All Bookings")
        print("5. Exit")

        choice = input("Enter your choice (1–5): ")

        if choice == "1":
            bookings.append(process_booking(Bus()))
        elif choice == "2":
            bookings.append(process_booking(Train()))
        elif choice == "3":
            bookings.append(process_booking(Flight()))
        elif choice == "4":
            print("\n🧾 Booking Summary:")
            if not bookings:
                print("No bookings yet.")
            else:
                for i, b in enumerate(bookings, 1):
                    print(f"{i}. {b}")
        elif choice == "5":
            print("\n👋 Thank you for using the Transport Booking System!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.")
