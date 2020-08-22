class Phone:
    def __init__(self, price):
        self.price = price

    def __sum__(self, other):
        return self.price + other.price


p1 = Phone(1000)
p2 = Phone(1200)
p3 = Phone(1000)

print(p1.price + p2.price)
