# function to take input from user
def takeInput():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+,-,*,/): ")
    return (num1, num2, operator)

# function to perform calculations and display result
def displayResult(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
        print(num1, "+", num2, "=", result)
    elif operator == '-':
        result = num1 - num2
        print(num1, "-", num2, "=", result)
    elif operator == '*':
        result = num1 * num2
        print(num1, "*", num2, "=", result)
    elif operator == '/':
        result = num1 / num2
        print(num1, "/", num2, "=", result)
    else:
        print("Invalid operator")

# main program
print("Calculator")
print("----------")
numbers = takeInput()
displayResult(numbers[0], numbers[1], numbers[2])
