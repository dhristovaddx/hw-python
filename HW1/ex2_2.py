def main():
    m = [1,24,55,21,6,8,10]
    z = input("Please enter a number: ")
    index = 0
    counter = 0
    match = True

    while(match):
        if (m[counter] + m[index] == int(z)):
            print(f"list[{counter}] + list[{index}] = {z}")
            match = False

        index += 1

        if(index == len(m)):
            index = 0
            counter += 1
         
main()