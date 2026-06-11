print("="*20 + " Welcome to Simple E-commerce Platform " + "="*20 + "\n")

# Login System
print("="*20 + "Login" + "="*20)
username = input("Enter username (admin/customer/cashier): ").strip().lower()
password = input("Enter password: ").strip()

role = ""

if username == "admin" and password == "admin123":
    role = "Admin"
elif username == "customer" and password == "cust123":
    role = "Customer"
elif username == "cashier" and password == "cash123":
    role = "Cashier"
else:
    print("Invalid username or password!")
    print("Program ended.")
    exit()

print(f"\nLogin successful! Welcome, {role}\n")

# Main Menu Loop
while True:
    print("\n=== Main Menu ===")
    
    if role == "Admin":
        print("1. View All Users")
        print("2. View Sales Report")
        print("3. Logout")
    elif role == "Customer":
        print("1. View Products")
        print("2. Make Purchase")
        print("3. Logout")
    elif role == "Cashier":
        print("1. Process Order")
        print("2. Logout")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "3" or (role == "Cashier" and choice == "2"):
        print("Logging out... Goodbye!")
        break
    # Admin Features
    elif role == "Admin":
        if choice == "1":
            print("\nUsers:")
            print("- admin (Admin)")
            print("- customer (Customer)")
            print("- cashier (Cashier)")
        elif choice == "2":
            print("\nSales Report:")
            print("Total Sales Today: $2450.75")
        else:
            print("Invalid choice!")
    
    # Customer Features
    elif role == "Customer":
        if choice == "1":
            print("\nAvailable Products:")
            print("- Laptop     : $899")
            print("- Headphones : $129")
            print("- T-shirt    : $25")
        elif choice == "2":
            print("\n=== Make Purchase ===")
            print("You can choose products.")
            print("Go to cashier to process your order and get receipt.")
            
            # adding items to cart
            total = 0.0
            print("\nEnter the prices of items you want to buy (enter 0 to finish):")
            
            while True:
                try:
                    price = float(input("Item price: $"))
                    if price == 0:
                        break
                    if price > 0:
                        total += price
                except:
                    print("Please enter a valid number.")
            
            print(f"\nYour Cart Subtotal: ${total:.2f}")
            print("Please go to the Cashier to apply discount, coupon and get final receipt.")
        
        else:
            print("Invalid choice!")
    
    # CASHIER Features
    elif role == "Cashier":
        if choice == "1":
            print("\n=== Process Customer Order ===")
            
            # Get subtotal from cashier
            subtotal = float(input("Enter Subtotal from Customer ($): "))
            
            # Discount based on subtotal
            discount = 0.0
            if subtotal >= 1000:
                discount = 0.15
                print("High value discount: 15% applied")
            elif subtotal >= 500:
                discount = 0.10
                print("Medium value discount: 10% applied")
            elif subtotal >= 100:
                discount = 0.05
                print("Basic discount: 5% applied")
            else:
                print("No discount applied")
            
            # Coupon Code
            coupon = input("Enter Coupon Code (or press Enter to skip): ").strip().upper()
            coupon_discount = 0.0
            
            if coupon == "SAVE10":
                coupon_discount = 0.10
                print("Coupon 'SAVE10' applied: 10% extra discount")
            elif coupon == "WELCOME5":
                coupon_discount = 0.05
                print("Coupon 'WELCOME5' applied: 5% extra discount")
            elif coupon != "":
                print("Invalid coupon code!")
            
            # Total discount 
            total_discount = discount + coupon_discount
            discounted_price = subtotal * (1 - total_discount)
            
            # Tax Calculation(8%)
            tax_rate = 0.08
            tax_amount = discounted_price * tax_rate
            final_price = discounted_price + tax_amount
            
            # Receipt (Issued by Cashier)
            print("\n" + "="*30)
            print("       OFFICIAL RECEIPT")
            print("="*30)
            print(f"Subtotal          : ${subtotal:.2f}")
            print(f"Discount Applied  : {total_discount*100:.1f}%")
            print(f"After Discount    : ${discounted_price:.2f}")
            print(f"Tax (8%)          : ${tax_amount:.2f}")
            print("-" * 30)
            print(f"FINAL AMOUNT      : ${final_price:.2f}")
            print("="*30)
            print("Thank you for shopping with us!")
            
        else:
            print("Invalid choice!")

print("\nThank you for using the system!")