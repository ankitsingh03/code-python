def num_sep(data):
    # data1 = []
    # for i in data:
    #     if type(i) == int:
    #         data1.append(i)
    # return data1
    return [str(i) for i in data if type(i)==int]

data = [True,1,False,{'name':'ankit'},2,('rohit','mohit'),3]
print(num_sep(data))

