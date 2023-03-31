# function to calculate the bill for a patient
def calculate_bill(name, cleaning, filling, xray):
    subtotal = 0
    if cleaning == 'y':
        subtotal += 60
    if filling == 'y':
        subtotal += 200
    if xray == 'y':
        subtotal += 100
    tax = subtotal * 0.15
    total = subtotal + tax
    if total > 300:
        total *= 0.9
    elif total > 200:
        total *= 0.95
    return (name, subtotal, tax, total)

# main program
print("Melanie Dental Clinic")
print("---------------------")
name = input("Enter patient's name: ")
cleaning = input("Was cleaning performed? (y/n): ")
filling = input("Was cavity-filling performed? (y/n): ")
xray = input("Was X-Ray performed? (y/n): ")
bill = calculate_bill(name, cleaning, filling, xray)
print("\nReceipt for patient name:", bill[0])
print("----------------------------------------------")
print("Subtotal: $", bill[1])
print("Tax: $", bill[2])
print("----------------------------------------------")
print("Total: $", bill[3])
