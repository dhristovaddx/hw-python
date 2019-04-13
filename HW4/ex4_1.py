def getFactorial(n):
    if n > 1:
      return n * getFactorial(n-1)
    elif n == 0:
      return 1
    else: 
      raise ValueError('Number should not be negative')

if __name__ == '__main__':
    try:
      num = int(input("Enter number: "))
      factorial = getFactorial(num)
      print(f"Factorial of {num} is {factorial}")
    except ValueError as e:
      print(e)