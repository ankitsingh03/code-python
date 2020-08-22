a = [{ "name" : "Nandini", "age" : 20},{ "name" : "Manjeet", "age" : 20 },{ "name" : "Nikhil" , "age" : 19 }]

print(sorted(a, key=lambda item:(item['age'], item['name'])))