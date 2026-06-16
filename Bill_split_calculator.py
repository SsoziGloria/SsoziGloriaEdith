bill_amount = int(input("What was the total bill amount?"))
if bill_amount <= 0:
    print("Invalid bill amount. Please enter a positive number.")
    exit()
Number_of_people = int(input("How many people are on the bill?"))
if Number_of_people <= 0:
    print("Invalid number of people. Please enter a positive number.")
    exit()

print("\nChoose a tip percentage:")
print("1. 10%")
print("2. 15%")
print("3. 20%")
print("4. custom")

Selection = input("Enter your selection(1-4): ")
if Selection == "1":
    Tip_percentage = 10
elif Selection == "2":
    Tip_percentage = 15
elif Selection == "3":
    Tip_percentage = 20
elif Selection == "4":
    Tip_percentage = int(input("Enter your custom tip percentage: "))
else:   
     print("Invalid selection. Defaulting to 10% tip.")
     Tip_percentage = 10

Tip_amount = bill_amount * (Tip_percentage / 100)
Total_bill = bill_amount + Tip_amount
Amount_per_person = Total_bill / Number_of_people

print("\n" + "=" *40)
print("\t BILL RECEIPT:")
print("=" *40)
print(f"Original bill amount:      UGX{bill_amount}")
print(f"Tip percentage:            {Tip_percentage}%")
print(f"Tip amount:                UGX{Tip_amount}")
print("-" *40)
print(f"Total bill after tip:      UGX{Total_bill}")
print(f"Number of people:          {Number_of_people}")
print(f"Amount per person:         UGX{Amount_per_person}")
print("=" *40)
print("Thank you!")
