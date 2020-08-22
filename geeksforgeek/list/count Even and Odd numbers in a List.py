a = (1,2,3,4,5,6,7,8,9)
even = tuple( i for i in a if i % 2 == 0)
odd = list(i for i in a if i % 2 != 0)
print(f"even is : {len(even)}, odd is : {len(odd)}")
