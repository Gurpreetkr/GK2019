# Passing Value
def squareOfNum(num):
    num = num * num
    print("square is{}".format(num))

n = 11
# squareOfNum(num=n)
squareOfNum(n)
print("n is:", n)

# Modifyinf num will not change n

def subtractNumbers(a, b, c):
    d = a-b-c
    print(d)

subtractNumbers(100, 20, 30)
subtractNumbers(a=100, b=20, c=30)