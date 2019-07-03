# Default Argument Values in Functions
def subtractNumbers(num1, num2, num3=0):
    subtraction = num1 - num2 - num3
    print("Subtraction is:", subtraction)

print("subtractNumbers is:", subtractNumbers)

# Update Operation on Functions
def subtractNumbers(num1, num2, num3=0, num4=0):
    subtraction = num1 - num2 - num3 - num4
    print("Subtraction is:", subtraction)

print("subtractNumbers is:", subtractNumbers)

subtractNumbers(100, 20)
subtractNumbers(1000, 200, 300)
