# global constants
PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

# function to take input from user
def takeInput():
    pennies = int(input("Enter the number of pennies: "))
    nickels = int(input("Enter the number of nickels: "))
    dimes = int(input("Enter the number of dimes: "))
    quarters = int(input("Enter the number of quarters: "))
    return (pennies, nickels, dimes, quarters)

# function to calculate total value
def calculateTotal(pennies, nickels, dimes, quarters):
    totalCent = pennies * PENNY_VALUE + nickels * NICKEL_VALUE + dimes * DIME_VALUE + quarters * QUARTER_VALUE
    totalDollars = totalCent / PENNIES_IN_DOLLAR
    return totalDollars

# main program
print("COUNT A DOLLAR")
print("-----------------")
numbers = takeInput()
totalDollars = calculateTotal(numbers[0], numbers[1], numbers[2], numbers[3])

if totalDollars > 1.0:
    print("Sorry, the amount you entered was more than one dollar.")
elif totalDollars < 1.0:
    print("Sorry, the amount you entered was less than one dollar.")
else:
    print("Congratulations!")
    print("The amount you entered was exactly one dollar!")
    print("You win the game!!")
