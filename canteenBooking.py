# Canteen Booking System

class Canteen:
    def __init__(self):
        self.menu = {
            1: {"Item": "Tea", "Price": 10},
            2: {"Item": "Coffee", "Price": 15},
            3: {"Item": "Sandwich", "Price": 30},
            4: {"Item": "Burger", "Price": 50},
            5: {"Item": "Pizza", "Price": 100},
        }
        self.orders = []

    def show_menu(self):
        print("\n===== 📋 Canteen Menu =====")
        for key, val in self.menu.items():
            print(f"{key}. {val['Item']} - ₹{val['Price']}")
        print()

    def place_order(self, item_no, quantity):
        if item_no in self.menu:
            item = self.menu[item_no]
            total_price = item["Price"] * quantity
            self.orders.append({"Item": item["Item"], "Quantity": quantity, "Total": total_price})
            print(f"✅ {quantity} x {item['Item']} booked successfully! (₹{total_price})\n")
        else:
            print("⚠️ Invalid item number.\n")

    def view_orders(self):
        if not self.orders:
            print("⚠️ No orders placed yet.\n")
            return
        print("\n===== 🧾 Your Orders =====")
        total_bill = 0
        for i, order in enumerate(self.orders, 1):
            print(f"{i}. {order['Item']} x {order['Quantity']} = ₹{order['Total']}")
            total_bill += order["Total"]
        print(f"💰 Total Bill: ₹{total_bill}\n")

    def cancel_order(self, order_no):
        if 0 <= order_no < len(self.orders):
            removed = self.orders.pop(order_no)
            print(f"🗑️ Order '{removed['Item']}' cancelled.\n")
        else:
            print("⚠️ Invalid order number.\n")


# -------- Main Program --------
def main():
    canteen = Canteen()

    while True:
        print("===== 🍴 Canteen Booking System =====")
        print("1. Show Menu")
        print("2. Place Order")
        print("3. View Orders")
        print("4. Cancel Order")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            canteen.show_menu()
        elif choice == "2":
            try:
                canteen.show_menu()
                item_no = int(input("Enter item number: "))
                quantity = int(input("Enter quantity: "))
                canteen.place_order(item_no, quantity)
            except ValueError:
                print("⚠️ Enter valid numbers.\n")
        elif choice == "3":
            canteen.view_orders()
        elif choice == "4":
            canteen.view_orders()
            try:
                order_no = int(input("Enter order number to cancel: ")) - 1
                canteen.cancel_order(order_no)
            except ValueError:
                print("⚠️ Enter a valid number.\n")
        elif choice == "5":
            print("👋 Thank you for using the Canteen Booking System!")
            break
        else:
