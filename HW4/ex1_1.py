def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def floorDivide(num1, num2):
    return num1 // num2

def quitApp():
    quit()

def calculate():
    action = {
         'a':add
        ,'s':subtract
        ,'m':multiply
        ,'d':divide
        ,'f':floorDivide
        ,'q':quitApp
    }
    ch = ''
    try:
        while ch != 'q':
            num1 = float(input("Enter 1st number:"))
            num2 = float(input("Enter 2nd number:"))
            ch = input('Enter a-add, s-subtract, m-multiply, d-divide, f-floor divide, q-quit:')
            if ch == 'q':
                print("Successfully exited the calculator")
                action[ch]()
            print(f'Result is {action[ch](num1, num2)}')
           
    except ValueError as e:
        print(f'Value error! Please enter a valid number ({e})')
        return calculate()
    except KeyError as e:
        print(f'Please enter a valid operation!')
        return calculate()
    except ZeroDivisionError as e:
        print(f'Cannot divide by 0')
        return calculate()

if __name__ == '__main__':
   result = calculate()
   print(f'result is {result}')

