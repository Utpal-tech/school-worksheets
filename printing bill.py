import datetime
date_time = datetime.datetime.now()
a = 61
invoice = "invoice"
invoicecenter = invoice.center(a, " ")

def bill():
    try:
        Item = input("enter name of item: ")
        unitPrice = float(input("enter unit price: "))
        quantity = float(input("Enter quantity: "))
        taxRate = float(input("enter tax% on item: "))
        value = unitPrice*quantity
        tax = (taxRate/100)*value
        total = value+tax




        print("-"*a)
        print(invoicecenter)
        print("-"*a)
        y =  date_time.year
        r = date_time.strftime("%m-%d %H:%M:%S")
        print("Date :"," "*35, y,"-",r, sep="")
        print("-"*a)
        print("Item", " "*15, "Unit Price", " "*5, "Quantity", " "*5, "Value")
        print("-"*a)
        print(Item," "*18, unitPrice, " "*10, quantity, " "*10, value)
        print("Tax:", " "*48, tax)
        print("-"*a)
        print("Amount Payable:", " "*37, total)
        conTinue()
    except:
        print("please enter correct input")
        conTinue()
def conTinue():
    print("do you want to print a bill\nenter y for yes or n for no")
    choice = input()
    if choice.lower() == "y":
        bill()
    elif choice.lower() == "n":
        print("thank you")
    else:
        print("you entered a wrong key")
        conTinye()
conTinue()
