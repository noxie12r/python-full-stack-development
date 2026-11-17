from abc import ABC, abstractmethod
from email.policy import default
class payment (ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class UPI (payment):
    def pay (self, amount):
        print (f"Paid {amount} using UPI")
class Card(payment):
    def pay (self, amount):
        print (f"Paid {amount} using Card")
p1 = UPI()
p2 = Card()
p1. pay (1000)
p2. pay (2000)