#WAP to input required values and find out and display the area of square.
def calculate():
    try:
        print("If you want to enter sides of the square then enter A\nIf you want to enter digonal enter B\nIf you want to enter perimeter enter C")
        var = input()
        if var.lower() == "a":
            side = float(input("Enter side of the square: "))
            area = side**2
            print("Area of the square with side",side,"is",area,"\n")
            conTinue()
        elif var.lower() == "b":
            dia = float(input("Enter the diagonal of the square: "))
            area = (dia/(2**(1/2)))**2
            print("Area of the square with diagonal",dia,"is",area,"\n")
            conTinue()
        elif var.lower() == "c":
            peri = float(input("Enter the perimeter of the squre: "))
            area = (peri/4)**2
            print("Area of the square with perimeter",peri,"is",area,"\n")
            conTinue()
        else:
            print("You entered a wrong key\n")
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
