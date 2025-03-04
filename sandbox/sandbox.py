def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper




@do_twice
def beegeek():
    print('beegeek')
    
print(beegeek())