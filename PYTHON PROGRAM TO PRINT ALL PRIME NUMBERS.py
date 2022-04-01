#PYTHON PROGRAM TO PRINT ALL PRIME NUMBERS 
#in a certain range

for i in range(1, 20):
    if i >= 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i)

TO FIND IF A NUMBER IS PRIME OR NOT
	num = int(input("Enter a number: "))
	if num > 1:
	    for i in range(2, num):
	        if (num % i) == 0:
	            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")
