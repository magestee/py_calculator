import os

def addition():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    continue_calculator = 'y'

    num1 = float(input("type your first numeber: "))
    num2 = float(input("type your second number: "))
    answer = num1 + num2
    values_entered = 2
    print(f"current result: {answer}")

    while continue_calculator.lower() == 'y':
        continue_calculator = input('enter more(y/n) ?: ')
        while continue_calculator.lower() not in ['y', 'n']:
            print("please ebter \"y\" or \"n\" ")
            continue_calculator = input('enter more(y/n) ?: ')
        if continue_calculator.lower() == 'n':
            break

        num = float(input("type another number to add to result: "))
        answer += num
        print(f"current result: {answer}")

        values_entered += 1
    return  [answer, values_entered]

def subtraction():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("subtraction:")

    num1 = int(input("type your first numeber: "))
    num2 = int(input("type your second number: "))

    return num1 - num2

def multipliction():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("multipliction:")

    num1 = int(input("type your first numeber: "))
    num2 = int(input("type your second number: "))

    return num1 * num2

def divion():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("division:")

    num1 = int(input("type your first numeber: "))
    num2 = int(input("type your second number: "))
 

    return num1 / num2

def calculator():
    quit = False

    while not quit:
        results = []
        print("simple calculator!")
        print("Enter \"a\" for addition ")
        print("Enter \"s\" for substraction ")
        print("Enter \"m\" for multipliction ")
        print("Enter \"d\" for division ")
        print("Enter \"q\" for quit ")

        choice = input("SELECT: ")

        if choice == "q":
            quit = True
            continue

        if choice == 'a':
            results = addition()
            print("answer: ", results[0], "total inputs enters: ", results[1])
        elif choice == "s":
            results = subtraction()
            print("answer: ", results)
        elif choice == "m":
            results = multipliction()
            print("answer: ", results)
        elif choice == "d":
            results = divion()
            print("answer: ", results)

if __name__ == '__main__':
    calculator()
