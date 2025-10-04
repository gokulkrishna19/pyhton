# restaurant_order_system.py
# Demonstrates Polymorphism with a Restaurant Order System

class Order:
    def take_order(self):
        raise NotImplementedError("Subclass must implement this method")


class MainDish(Order):
    def take_order(self):
        dish = input("🍛 Enter main dish name: ")
        qty = int(input("Enter quantity: "))
        print(f"✅ {qty} {dish}(s) ordered!\n")
        return f"Main Dish → {dish} x {qty}"


class Drink(Order):
    def take_order(self):
        drink = input("🥤 Enter drink name: ")
        qty = int(input("Enter quantity: "))
        print(f"✅ {qty} {drink}(s) ordered!\n")
        return f"Drink → {drink} x {qty}"


class Dessert(Order):
    def take_order(self):
        sweet = input("🍰 Enter dessert name: ")
        qty = int(input("Enter quantity: "))
        print(f"✅ {qty} {sweet}(s) ordered!\n")
        return f"Dessert → {sweet} x {qty}"


# Polymorphic function
def take(order_type):
    return order_type.take_order()


# -------- Main Program --------
if __name__ == "__main__":
    print("===== 🍴 Restaurant Order System =====")

    orders = []
    while True:
        print("\n1. Main Dish")
        print("2. Drink")
        print("3. Dessert")
        print("4. Show Orders")
        print("5. Exit")

        choice = input("Enter your choice (1–5): ")

        if choice == "1":
            orders.append(take(MainDish()))
        elif choice == "2":
            orders.append(take(Drink()))
        elif choice == "3":
            orders.append(take(Dessert()))
        elif choice == "4":
            print("\n🧾 Your Orders:")
            if not orders:
                print("No orders placed yet.")
            else:
                for i, o in enumerate(orders, 1):
                    print(f"{i}. {o}")
        elif choice == "5":
            print("\n👋 Thank you for dining with us!")
            break
        else:
            print("⚠️ Invalid choice, please try again.")
