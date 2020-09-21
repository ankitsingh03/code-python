"""
      *
   *  *  *
*  *  *  *  *
   *  *  *
      *
"""
n = 7
lst = []
for i in range(1, n+1, 2):
    lst.append('*  ' * i)
for i in range(len(lst)):
    print("   " * (len(lst)-i-1) + lst[i])
for i in range(len(lst)-2, -1, -1):
    print("   " * (len(lst)-i-1) + lst[i])
