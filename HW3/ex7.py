from functools import wraps

def to_list(func):
    @wraps(func)
    def wrapper(*args):
        args = func(*args)
        value = []
        for v in args:
            value.append(f'{v}')
            yield value
    return wrapper

# Въпрос: Как може чрез floor division и с % да взима цифрите на числото от ляво на дясно, а не от дясно на ляво?
#@to_list
#def gen_digits(n):
#    while n > 0:
#        d = n % 10
#        n //= 10
#        yield d

@to_list
def gen_digits(n):
    for i in str(n):
        digit = int(i)
        yield digit

if __name__ == '__main__':
    x = 123
    g = gen_digits(x)
    print(next(g))
    print(next(g))
    print(next(g))

    