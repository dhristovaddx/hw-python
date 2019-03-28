def cmap(func, iterable):
    i = 0

    for item in iterable:
        iterable[i] = func(item)
        i += 1
        
    return iterable

def getFactorial(n):
    if n == 1:
        return n
    else:
        return n * getFactorial(n-1)
    

if __name__ == '__main__':
    m = [1, 3, 5]
    result = cmap(getFactorial, m)
    print(f"Result is {result}")