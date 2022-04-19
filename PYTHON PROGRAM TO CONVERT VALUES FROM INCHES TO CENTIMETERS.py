# inches to centimeter
# 1 inch = 2.54 cm
from re import A


x = int(input("enter a value :"))


def product(x):
    for i in range(0, x):
        product = x*2.54
        print(product)
        break


product(x)
