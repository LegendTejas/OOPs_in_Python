from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentSystem):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}... Approved!")

class PayPalPayment(PaymentSystem):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}... Approved!")

# Using different payment systems via abstraction
def complete_purchase(payment_processor, amount):
    payment_processor.process_payment(amount)

complete_purchase(CreditCardPayment(), 250)
complete_purchase(PayPalPayment(), 99.99)
