#WAP to print the sum of digits present if number is 256.
print("This program prints the sum of digits present in number 256\n")
num = 256
numInStr = str(num)
length = len(numInStr)
sUm = 0
for i in range (0,length):
    a = int((numInStr[i]))
    sUm = sUm+a
print("Sum of all digits in",num,"is",sUm,"\n")
