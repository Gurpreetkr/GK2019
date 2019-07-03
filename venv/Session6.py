# Functions - f(x) = x*x
#             f(x) = 2*2 = 4
# Methods/ Procedures/ Routines

"""
   Functions
   1. Name
   2. Inputs(May or May Not) | Parameters | Arguments
   3. return(May or May Not) | Acknowledgement
   4. Definition(May or May Not) --> Sequence

   Why Loops ?
       Where we write statements which
       are repeated again and again
   Why Functions ?
       Group of statements / logic which has
       to be executed again and again

   Modularization is something which we are doing
   in our program to simpify the process
"""

#Definition of Function : addNumbers
#num1 and num2 are inputs
def subtractNumbers(num1, num2):
    num3 = num1 - num2
    print("Subtraction of {} and {} is {}".format(num1, num2, num3))
    return num3

result = subtractNumbers(50, 20) # Execution of subtractNumbers Function
print("Subtraction is:", result)
print(subtractNumbers(70, 30))
print("Subtraction is:", subtractNumbers(85, 50))
print(subtractNumbers(12,-67))
