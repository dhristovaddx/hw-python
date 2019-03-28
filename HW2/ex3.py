def sumNumbers(l):
    total = 0
    
    for i in l:
        if type(i) is list:
            total = total + sumNumbers(i)
        else:
            total = total + i
    return total

if __name__ == '__main__':
    m = [1,2,3,[5,6,[7]],4]
    result = sumNumbers(m)
    print(f"Sum is {result}")

