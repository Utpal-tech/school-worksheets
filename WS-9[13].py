'''WAP to input the names and the basic salary of a person and print his take home pay.
HRA =20% of Basic salary
DA = 98% of basic salary
PF = 8.33% OF Basic salary
Gross pay = Basic salary + HRA +DA
IT = 20% of Gross Pay
Deduction = PF + IT
Take home pay = Gross pay – Deduction'''


print("This program takes name and basic salary of a person as input and prints his take home pay\n")

def calculate():
    try:
        name = input("Enter your name: ")
        basicSalary = float(input("Enter your Basic Salary: "))
        HRA = (20/100)*basicSalary
        DA = (98/100)*basicSalary
        PF = (8.33/100)*basicSalary
        grossPay = basicSalary + HRA + DA
        IT = (20/100)*grossPay
        deduction = PF + IT
        takeHomePay = grossPay - deduction
        print("\nTake home pay of",name,"with basic salary",basicSalary,"is",takeHomePay,"\n")
        conTinue()
    except:
        print("\nPlease provide correct input")
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