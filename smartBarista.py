#Declare the variables
header_Menu= "Menu".center(30,"=")
drink_Item1= "Bosspresso"
drink_Price1= "RM8.50"
drink_Item2= "Eiskaffee"
drink_Price2= "RM12.50"


#Greet customers
customer_Name = input("Please enter your name:\n").capitalize()
print(f"Hello, {customer_Name}! Welcome to Dus Coffee.\n")
print(header_Menu)
print(drink_Item1.ljust(20) + drink_Price1.rjust(10))
print(drink_Item2.ljust(20) + drink_Price2.rjust(10))

#Enter menu price
customer_Price=float(input("Please enter the price of the drinks you choose:\nRM"))

#short name logic
if (len(customer_Name) <=3):
    print(f"{customer_Name}, you make us easy to call your name, so we give you discount!")
    customer_Price = customer_Price - 1.50
    print(f"RM{customer_Price:0.2f}")


#tax and tip calculation
tax_drinkPrice = customer_Price * 0.10
tip_drinkPrice = customer_Price * 0.15

#final receipt
print(f"Total price: RM{tax_drinkPrice + tip_drinkPrice + customer_Price:0.2f}")
print(f"Please wait, we will call you once drink(s) is ready. Have a nice day, {customer_Name}!")

