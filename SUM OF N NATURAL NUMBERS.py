

from re import A
num = int(input("enter a value"))


def sum(num):
    for i in range(0, num):
        A = (num+1)/2
        B = num*A
        print(B)
        break


sum(num)
