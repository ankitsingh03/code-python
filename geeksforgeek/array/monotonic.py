a = [6,5,4,4]
print(all(a[i] <= a[i+1] for i in range(len(a)-1)))