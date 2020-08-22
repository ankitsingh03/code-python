import time
def calculate_time(function):
    def wrapper(*args):
        t1=time.time()
        a = function()
        t2=time.time()
        print(t2-t1)
        return a
    return wrapper

@calculate_time
def func():
    return ("this is function")

func()
