from functools import wraps
from math import log10, floor, ceil

def to_list(func):
    @wraps(func)
    def wrapper(*args):
        for v in [str(i) for i in func(*args)]:
            yield v
    return wrapper

@to_list
def gen_digits(num):
	numDigits = floor(log10(num))
	while numDigits >= 0:
		digit = num // 10**numDigits % 10
		yield digit
		numDigits -= 1


if __name__ == '__main__':
    x = 123
    g = list(gen_digits(x))
    print(g)

    