class ParanthesisNotBalanced(Exception):
    pass

def checkParanthesis(str1):
      counter = 0
      for ch in str1:
          if ch == '(':
              counter += 1
          elif ch == ')':
              counter -= 1 
      
      if counter == 0:
        return True
      else:
        raise ParanthesisNotBalanced('Please check your parenthesis! Not balanced!')
        

if __name__ == '__main__':
    str1 = '((()())())'
    try:
      check = checkParanthesis(str1)
      print(f'Parenthesis {str1} are balanced!')
    except ParanthesisNotBalanced as e:
      print(e)