def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return(x * y)
def divide(x,y):
    if y==0:
        return "Error: cannot be divided by zero"
    else:
        return x/y
    
def show_menu():
    print("\n" +"="*5+ "Calculator Menu" + "="*5)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("="*20)

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please enter a number from 1 to 5.")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        result = add(a, b)
        print(f"Result: {a} + {b} = {result}")

    elif choice == "2":
        result = subtract(a, b)
        print(f"Result: {a} - {b} = {result}")

    elif choice == "3":
        result = multiply(a, b)
        print(f"Result: {a} * {b} = {result}")

    elif choice == "4":
        result = divide(a, b)
        if result is not None:
            print(f"Result: {a} / {b} = {result}")
    




