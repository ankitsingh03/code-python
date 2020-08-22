def func(*args):
    avg = []
    for pair in zip(*args):
        avg.append(sum(pair)/len(pair))
    return avg

print(func([1,2,3],[4,5,6]))
