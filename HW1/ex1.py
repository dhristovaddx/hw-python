def add(num1, num2):
    print(int(num1) + int(num2))

def subtract(num1, num2):
    print(int(num1) - int(num2))

def multiply(num1, num2):
    print(int(num1) * int(num2))

def divide(num1, num2):
    print(int(num1) / int(num2))

def floorDivide(num1, num2):
    print(int(num1) // int(num2))

def quitApp():
    print("Successfully exited the calculator")

def main():
    action = {
         'a':add
        ,'s':subtract
        ,'m':multiply
        ,'d':divide
        ,'f':floorDivide
    }
    ch = ''

    while ch != 'q':
        num1 = input("Enter 1st number:")
        num2 = input("Enter 2nd number:")
        ch = input('Enter a-add, s-subtract, m-multiply, d-divide, f-floor divide, q-quit:')
        
        if ch in action:
            action[ch](num1, num2)
        elif ch == 'q':
            quitApp()
        else:
            print('Invalid option:{}'.format(ch))
        
main()

