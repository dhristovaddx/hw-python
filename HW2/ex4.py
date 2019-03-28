def getFactorial(n):
    if n == 1:
        return n
    else:
        return n * getFactorial(n-1)

if __name__ == '__main__':
    num = int(input("Enter number: "))
    factorial = getFactorial(num)
    print(f"Factorial of {num} is {factorial}")