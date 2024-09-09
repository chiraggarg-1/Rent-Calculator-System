print("WELCOME TO RENT CALCULATOR SYSTEM")
total_rent = 0
hostel_rent = int(input("Enter your hostel/flat Rent "))
total_rent += hostel_rent
print(f"Your house rent is {hostel_rent} Rs")
food_expense = int(input("Enter your food Expenses "))
total_rent += food_expense
print(f"Your Food Expense is {food_expense} Rs")
electricty_unit = int(input("Enter the electricity units you have consumed "))
elec_unit_charge = int(input("Enter the charge per unit of electricity"))
elec_bill = electricty_unit * elec_unit_charge
total_rent += elec_bill
print(f"Your electricity Bill is {elec_bill} Rs")
print(f"YOUR TOTAL EXPENSE IS {total_rent} Rs ")
total_member = int(input("How many total members live Together "))
each_Person_Share = total_rent/total_member
print(f"Each Person Will have to pay {each_Person_Share} Rs ")
print("TAHNK YOU !!!😎")