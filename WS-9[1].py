#WAP to input three numbers and print their sum, product and differences.
print("This program will take 3 inpur and calculate their sum and product.")
def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        sUm = num1+num2+num3
        product = num1*num2*num3
        dif1 = num1-num2-num3
        dif2 = num2-num3-num1
        dif3 = num3-num2-num1
        print("Sum of",num1,",",num2,"and",num3,"is",sUm,"\n")
        print("Product of",num1,",",num2,"and",num3,"is",product,"\n")
        print("The value of",num1,"-",num2,"-",num3,"is",dif1,"\n")
        print("the value of",num2,"-",num1,"-",num3,"is",dif2,"\n")
        print("and the value of",num3,"-",num1,"-",num2,"is",dif3,"\n")
        conTinue()
    except:
        print("Please provide correct input\n")
        conTinue()


def conTinue():
    print("Do you want to calculate.\nEnter Y for yes and N for no")
    userInput = input()
    if userInput.lower() == "y":
        calculator()
    elif userInput.lower():
        print("Thank You")
    else:
        print("Please provide correct input\n")
        conTinue()


calculator()
    