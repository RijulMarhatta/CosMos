# PYTHON PROGRAM FOR COMPOUND INTEREST
p = int(input("enter the principal amount:"))
r = float(input("enter the rate of interest:"))
t = int(input("enter the time span:"))
a = p * (pow((1+(r/100)), t))
ci = a-p
print(ci)
