#WAP to input two numbers and print the product of their sum and differences.
print("This program will take 2 float inputs and calculate the product of their sum and difference")
def calculate():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        sUm = num2+num1
        difference1 = num1-num2
        difference2 = num2-num1
        print("Product of (",num1,"+",num2,") and (",num1,"-",num2,") is",sUm*difference1)
        print("Product of (",num1,"+",num2,") and (",num2,"-",num1,") is",sUm*difference2)
        conTinue()
    except:
        print("Please provide correct input")
        conTinue()
def conTinue():
    print("\nDo you want to calculate again\nEnter Y for yes and N for no.")
    retry = input()
    if retry.lower() == "y":
        calculate()
    elif retry.lower() == "n":
        print("Thank you")
    else:
        print("Please provide correct input")
        conTinue()


calculate()