class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, discount):
        self.price = self.price - (self.price * discount / 100)
        print("New Price =", self.price)


laptop = Laptop("Dell", 50000)

laptop.apply_discount(10)