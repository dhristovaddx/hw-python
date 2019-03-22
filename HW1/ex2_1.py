def main():
    m = [1,24,55,21,6,8,10]
    z = input("Please enter a number: ")

    for key, i in enumerate(m):
      for key2, j in enumerate(m):
        if (i + j == int(z)):
            print(f"m[{key}] + m[{key2}] = {z}")
            return
         
main()