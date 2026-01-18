while True:                                                            # if True, the loop will run continuously without stopping
    
    print("----------------------------")                              # prints a dividing line
    num1 = float(input("Enter the first number: "))                    # defines the variable num1; float allows decimal numbers
    num2 = float(input("Enter the second number: "))                   # defines the variable num2; float allows decimal numbers
   
    print("----------------------------")                              # prints a dividing line
    print("Choose the operation you want:")                            # displays the text and options
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")

    op = input("Enter the number of the chosen operation: ")           # defines the variable 'op' as the chosen operation

    if op == "1":                                                      # if op is 1, performs addition and prints the result
        print("Result:", num1 + num2)
    elif op == "2":                                                    # elif means "else if"; if op is 2, performs subtraction and prints the result
        print("Result:", num1 - num2)           
    elif op == "3":                                                    # elif; if op is 3, performs multiplication and prints the result
        print("Result:", num1 * num2)                 
    elif op == "4":                                                    # elif; if op is 4, performs division and prints the result
        print("Result:", num1 / num2)
    else:                                                              # else means "otherwise"; executes if none of the previous conditions are met
        print("Invalid operation")                                     # prints a message indicating the operation is invalid
