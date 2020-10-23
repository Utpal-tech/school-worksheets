#WAP to print the number in the reverse order, if number is 123.
print("This program prints number 123 in reverse order\n")
num = 123
numInStr = str(num)
i = len(numInStr)-1
print(num," in reverse is ", sep="", end="")
while i>= 0:
    print(numInStr[i], sep="", end="")
    i = i-1