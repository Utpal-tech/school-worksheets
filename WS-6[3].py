#WAP to input temperature in Celsius and convert it into Fahrenheit using the formula:F=1.8 * C +32
def calculate():
    try:
        c = float(input("Enter the temperature in celsius: "))
        f = 1.8*c+32
        print("Temperature in Fahrenheit is",f,"\n")
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