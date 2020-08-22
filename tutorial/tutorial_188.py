class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def discount(self,percent):
        per = self.price - (self.price*(percent/100))
        return per


l1 = Laptop('dell','inspiron',50000)
l2 = Laptop('lenovo', 'yoga', 40000)
print(l1.brand_name)
print(l1.discount(10))
