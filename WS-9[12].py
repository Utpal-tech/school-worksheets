#WAP to input the side of a triangle (a, b & c) and calculate
# its area by using the formula given Area= square root of (s* (s-a)*(s-b)*(s-c)), where s= (a+b+c)/2.
#WAP to enter a three digit number and print its digit it in reverse order.
print("This program takes the length of three side of a triangle as input and prints its area\n")

def calculate():
    try:
        a = float(input("Enter the length of first side: "))
        b = float(input("Enter the length of second side: "))
        c = float(input("Enter the length of third side: "))
        if (a+b)<c or (a+c)<b or (b+c)<a:
            print("\nTriangle cannot be constructed with the given sides, check your entry.")
            conTinue()
        else:
            s = (a+b+c)/2
            area = (s*(s-a)*(s-b)*(s-c))**(1/2)
            print("\nArea of triangle of side lengths",a,",",b,"and",c,"is",area,"\n")
            if area==0:
                print("Here area = 0 denotes that three line which make the triangle are on a the same straight line.")
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