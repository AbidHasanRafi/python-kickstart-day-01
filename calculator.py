while True:  
    print("\nSimple Python Calculator")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting Calculator. Thank you!")
        break  # Exit the loop

    if choice in ['1', '2', '3', '4']:  
        num1 = float(input("Enter first number: "))  
        num2 = float(input("Enter second number: "))  

        if choice == '1':  
            result = num1 + num2  
            print(num1, "+", num2, "=", result)  

        elif choice == '2':  
            result = num1 - num2  
            print(num1, "-", num2, "=", result)  

        elif choice == '3':  
            result = num1 * num2  
            print(num1, "*", num2, "=", result)  

        elif choice == '4':  
            if num2 == 0:  
                print("Error: Cannot divide by zero!")  
            else:  
                result = num1 / num2  
                print(num1, "/", num2, "=", result)  

    else:  
        print("Invalid choice! Please enter a number between 1-5.")  