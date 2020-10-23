#WAP to input the mass and velocity and find out and display the Kinetic Energy.Use formula: Ke=1/2 mv2
print("This Program will take 2 float input as mass and velocity and calculate the kinetic energy of the system.")

def calculate():
    try:
        mass = float(input("Enter mass of the system: "))
        velocity = float(input("Enter velocity of the system: "))
        k_e = 1/2*(mass*velocity)
        print("Kinetic energy of the system is",k_e,"\n")
        conTinue()
    except:
        print("Please provide correct input\n")
        conTinue()
def conTinue():
    print("Do you want to calculate again\nEnter Y for yes and N for no.\n")
    retry = input()
    if retry.lower() == "y":
        calculate()
    elif retry.lower() == "n":
        print("Thank you\n")
    else:
        print("Please provide correct input\n")
        conTinue()


calculate()