#WAP to input a number and prints it square and cube.
print("This program will take a inputs and calculate its squre and cube.")
def calculate():
    try:
        num1 = float(input("Enter first number: "))
        print("Squre of",num1,"is",num1**2,"and its cubeis",num1**3,)
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
