#WAP to input principal, rate and time and find out and display the Simple Interest. SI=P * R * T/100
def calculate():
    try:
        p = float(input("Enter principle: "))
        r = float(input("Enter rate: "))
        t = float(input("Enter time in years: "))
        si = (p*r*t)/100
        print("Simple Interest on",p,"with",r,"% of rate for",r,"years of time is",si,"\n")
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