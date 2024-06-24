def calculator():
    print("Welcome to Simple Calculator!")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    
    # Take input from the user
    choice = input("Enter operation number (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == '3':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
    elif choice == '4':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    else:
        print("Invalid input. Please enter a valid operation number (1/2/3/4).")
    
    # Ask user if they want to perform another calculation
    try_again = input("Do you want to perform another calculation? (yes/no): ").lower()
    if try_again == 'yes' or try_again == 'y':
        calculator()
    else:
        print("Thank you for using the calculator. Goodbye!")

# Call the calculator function to start the program
calculator()

