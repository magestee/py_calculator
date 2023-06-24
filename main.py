def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multipliction(num1, num2):
    return num1 * num2

def divion(num1, num2):
    return num1 / num2

num1 = int(input("type your first numeber: "))
num2 = int(input("type your second number: "))

addition_result = addition(num1, num2)
subtraction_result = subtraction(num1, num2)
multipliction_result = multipliction(num1, num2)
division_result = divion(num1, num2)

print("addition result is: ", addition_result)
print("subtraction result is: ", subtraction_result)
print("multipliction result is: ", multipliction_result)
print("division result is: ", division_result)