def checkParanthesis(str1):
    counter = 0

    for ch in str1:
        if ch == '(':
            counter += 1
        elif ch == ')':
            counter -= 1
        else:
          return False

    if counter == 0:
        return True

if __name__ == '__main__':
    str1 = '((()())())'
    check = checkParanthesis(str1)
    print(f'Parenthesis {str1} are balanced: {check}')