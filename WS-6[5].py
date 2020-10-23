#WAP to input a number of seconds and prints it is form: (Min : Sec)
def calculate():
    try:
        time = int(input("Enter time in second: "))
        m = time//60
        s = (time%60)
        print(time,"s in minutes and second in formet (min : sec) is",m,":",s,"\n")
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
