# Total food orders
#electricity bill unit spend
#charge per unit
#person living in room

# output
#total amount you are to pay is

rent =int(input("Enter your room rent:-"))
food=int(input("Enter the amount of food/rashan orderd:-"))
electricity_unit=int(input("Enter the electricity unit spend:-"))
charge_per_unit=int(input("Enter the charge per unit:-"))
person=int(input("Enter the number of person living in room:-"))

total_bill=electricity_unit*charge_per_unit

output =(food +rent+total_bill)//person
print("Each person will pay ",output)
