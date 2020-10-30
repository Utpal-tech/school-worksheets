#WAP to input three numbers and display them on different lines by using single print statement.
def calculate():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        print(num1,num2,num3,sep="\n")
        conTinue()  
    except:
        print("Please enter a correct velue\n")
        conTinue()
def conTinue():
    print("Do you want to calulate again.\nEnter Y for Yes or N for No")
    choice = input()
    if choice.lower() == "y":
        calculate()
    elif choice.lower() == "n":
        print("Thank you")
    else:
        print("You entered a wrong key\n")
        conTinue()
calculate()
