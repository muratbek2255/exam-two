import numbers

def func(*args):
    result = 0
    for i in args:
        if isinstance(i, numbers.Number):
            return result






