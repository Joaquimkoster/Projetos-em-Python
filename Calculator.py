while True:                                                            # Start an infinite loop to keep the program running
    
    print("----------------------------")                              # Print a visual separator for better readability
    num1 = float(input("Enter the first number: "))                    # Prompt user for input and convert it to a floating-point number
    num2 = float(input("Enter the second number: "))                   # Prompt user for second input and convert it to a floating-point number
   
    print("----------------------------")                              # Print another visual separator
    print("Choose the operation you want:")                            # Display the header for the operation menu
    print("1) Addition")                                               # Display option 1 for addition
    print("2) Subtraction")                                            # Display option 2 for subtraction
    print("3) Multiplication")                                         # Display option 3 for multiplication
    print("4) Division")                                               # Display option 4 for division

    op = input("Enter the number of the chosen operation: ")           # Capture the user's menu choice as a string

    if op == "1":                                                      # Check if the user selected '1' (Addition)
        print("Result:", num1 + num2)                                  # Calculate and display the sum of num1 and num2
    elif op == "2":                                                    # Check if the user selected '2' (Subtraction)
        print("Result:", num1 - num2)                                  # Calculate and display the difference
    elif op == "3":                                                    # Check if the user selected '3' (Multiplication)
        print("Result:", num1 * num2)                                  # Calculate and display the product
    elif op == "4":                                                    # Check if the user selected '4' (Division)
        if num2 != 0:                                                  # Nested check to ensure the divisor is not zero
            print("Result:", num1 / num2)                              # Calculate and display the quotient
        else:                                                          # Execute if num2 is zero
            print("Error: Division by zero!")                          # Display an error message to prevent a crash
    else:                                                              # Execute if the input 'op' matches none of the above
        print("Invalid operation, try again")                          # Notify the user their input was not a valid choice

    while True:                                                        # Start a nested loop to handle the exit confirmation
        exit_choise = input("Do you want to exit? (y/n): ").strip().lower().replace(" ","") # Clean user input (remove spaces/lowercase)

        if exit_choise == "y":                                         # Check if the user wants to quit
            exit()                                                     # Terminate the entire program immediately
        elif exit_choise == "n":                                       # Check if the user wants to continue
            print("restarting...")                                     # Inform the user the calculator is resetting
            break                                                      # Break the inner loop to return to the main calculator loop
        else:                                                          # Handle cases where input is not 'y' or 'n'
            print("Invalid option, please type 'y' for yes or 'n' for no.") # Prompt for a valid response