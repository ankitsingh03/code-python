months = ["january", "february", "march", "april", "may"]
exp = [2200, 2350, 2600, 2130, 2190]

# february - january
print(exp[months.index("february")] - exp[months.index("january")])

# three months expenses
print(exp[months.index("january")] + exp[months.index("february")] + exp[months.index("march")])

# 2000 dollar in any months
for i, j in enumerate(exp):
    if 2000 == j:
        print(True)
        break
else:
    print(False)

# add june 1980
months.append("june")
exp.append(1980)

# return an item that i got in april months 200 dollar
exp[months.index("april")] = exp[months.index("april")] - 200
print(exp)
