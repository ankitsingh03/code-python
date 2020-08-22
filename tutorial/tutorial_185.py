class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price


l1 = Laptop('dell','inspiron',39000)
l2 = Laptop('lenovo', 'yoga', 40000)
print(l1.brand_name)