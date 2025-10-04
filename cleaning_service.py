# cleaning_service.py
# Demonstrates Polymorphism in a Cleaning Service System

class CleaningService:
    def perform_service(self):
        raise NotImplementedError("Subclass must implement this method")


class HomeCleaning(CleaningService):
    def perform_service(self):
        rooms = int(input("🏠 Enter number of rooms to clean: "))
        print(f"✅ Home cleaning scheduled for {rooms} room(s).\n")
        return f"Home Cleaning → {rooms} room(s)"


class OfficeCleaning(CleaningService):
    def perform_service(self):
        desks = int(input("🏢 Enter number of desks to clean: "))
        print(f"✅ Office cleaning scheduled for {desks} desks.\n")
        return f"Office Cleaning → {desks} desks"


class VehicleCleaning(CleaningService):
    def perform_service(self):
        vehicles = int(input("🚗 Enter number of vehicles to clean: "))
        print(f"✅ Vehicle cleaning scheduled for {vehicles} vehicle(s).\n")
        return f"Vehicle Cleaning → {vehicles} vehicle(s)"


# Polymorphic function
def book_service(service_type):
    return service_type.perform_service()


# -------- Main Program --------
if __name__ == "__main__":
    print("===== 🧽 Cleaning Service Management =====")

    services = []
    while True:
        print("\n1. Home Cleaning")
        print("2. Office Cleaning")
        print("3. Vehicle Cleaning")
        print("4. View All Bookings")
        print("5. Exit")

        choice = input("Enter your choice (1–5): ")

        if choice == "1":
            services.append(book_service(HomeCleaning()))
        elif choice == "2":
            services.append(book_service(OfficeCleaning()))
        elif choice == "3":
            services.append(book_service(VehicleCleaning()))
        elif choice == "4":
            print("\n🧾 Service Bookings:")
            if not services:
                print("No bookings yet.")
            else:
                for i, s in enumerate(services, 1):
                    print(f"{i}. {s}")
        elif choice == "5":
            print("\n👋 Thank you for choosing Sparkle Cleaning Services!")
            break
        else:
            print("⚠️ Invalid choice! Try again.")
