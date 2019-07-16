num = 20

def show():

    global num

    num = num % 4
    print("1. num is:",num)

show()
print("2. num is:",num)

age = 25

"""
cart = []
def addProductToCart(product):
    global cart
    cart.append(product)
"""