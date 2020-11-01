#WAP to enter a three digit number and print its digit it in reverse order.
print("This program take a three digit number as input and prints it in reverse order\n")

def calculate():
    try:
        num = input("Enter a number: ")
        if len(num)>3 or len(num)<3:
            print("\nplease enter a correct number")
            conTinue()
        else:
            i = len(num)-1
            print(num," in reverse is ", sep="", end="")
            while i>= 0:
                print(num[i], sep="", end="")
                i = i-1
            conTinue()
    except:
        print("Please provide correct input")
        conTinue()
def conTinue():
    print("\n\nDo you want to calculate again\nEnter Y for yes and N for no.")
    retry = input()
    if retry.lower() == "y":
        calculate()
    elif retry.lower() == "n":
        print("Thank you")
    else:
        print("Please provide correct input")
        conTinue()


calculate()
