#WAP to input two numbers and print the sum of 25% of each number.
print("This Program will take 2 float input and calculate the sum of 25% of each number.")

def calculate():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        sUm = 25/100*(num2+num1)
        print("Sum of 25% of",num1,"and",num2,"is",sUm)
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