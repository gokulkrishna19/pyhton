# order_system.py
# Demonstrates Polymorphism with an Order-Taking System

class Order:
    def place_order(self):
        raise NotImplementedError("Subclass must implement this method")


class FoodOrder(Order):
    def place_order(self):
        item = input("🍔 Enter the food item you want to order: ")
        qty = int(input("Enter quantity: "))
        print(f"✅ {qty} {item}(s) ordered successfully!\n")
        return f"Food Order → {qty} x {item}"


class DrinkOrder(Order):
    def place_order(self):
        item = input("🥤 Enter the drink you want to order: ")
        qty = int(input("Enter quantity: "))
        print(f"✅ {qty} {item}(s) ordered successfully!\n")
        return f"Drink Order → {qty} x {item}"


class DessertOrder(Order):
    def place_order(self):
        item = input("🍰 Enter the dessert you want to order: ")
        qty = int(input("Enter quantity: "))
        print(f"✅ {qty} {item}(s) ordered successfully!\n")
        return f"Dessert Order → {qty} x {item}"


# ---- Polymorphism in action ----
def take_order(order_type):
    return order_type.place_order()


# -------- Main Program --------
if __name__ == "__main__":
    print("===== 🍽️ Welcome to QuickServe Order System =====")

    orders = []
    while True:
        print("\n1. Food Order")
        print("2. Drink Order")
        print("3. Dessert Order")
        print("4. Show All Orders")
        print("5. Exit")

        choice = input("Enter your choice (1–5): ")

        if choice == "1":
            orders.append(take_order(FoodOrder()))
        elif choice == "2":
            orders.append(take_order(DrinkOrder()))
        elif choice == "3":
            orders.append(take_order(DessertOrder()))
        elif choice == "4":
            print("\n🧾 Orders Summary:")
            if not orders:
                print("No orders placed yet.")
            else:
                for i, o in enumerate(orders, 1):
                    print(f"{i}. {o}")
        elif choice == "5":
            print("\n👋 Thank you for using QuickServe! Visit again!")
            break
        else:
            print("⚠️ Invalid choice! Try again.")
