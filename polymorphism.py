# Polymorphism Example: Payment System

class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclass must implement this method")

class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"💳 Paid ₹{amount} using Credit Card."

class DebitCardPayment(Payment):
    def pay(self, amount):
        return f"🏦 Paid ₹{amount} using Debit Card."

class UpiPayment(Payment):
    def pay(self, amount):
        return f"📱 Paid ₹{amount} using UPI."

# Function that works with any type of Payment (Polymorphism)
def process_payment(payment_method, amount):
    print(payment_method.pay(amount))


# -------- Main Program --------
if __name__ == "__main__":
    # Different payment options
    payments = [
        CreditCardPayment(),
        DebitCardPayment(),
        UpiPayment()
    ]

    # Same function call → different behaviors
    for method in payments:
        process_payment(method, 500)
