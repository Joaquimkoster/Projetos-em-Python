import random                                                               # allows you to use functions that generate random numbers or make random choices in Python

while True:                                                                 # infinite loop that will run until explicitly broken
    print("====== Password Generator ======")                               # prints the title
    
                                                                            # asks the user how many characters they want in the password
    char_count = int(input("Enter the number of characters: "))             # converts input to an integer so it can be used in calculations
    
                                                                            # calculates the smallest number with the desired number of digits
    lower = 10 ** (char_count - 1)  
    
                                                                            # calculates the largest number with the desired number of digits
    upper = (10 ** char_count) - 1  
    
                                                                            # generates a random number between lower and upper
    password = random.randint(lower, upper)  
    
    print("Your new password is", password)                                 # displays the generated password
    
                                                                            # asks the user if they want to exit the program
    response = input("Do you want to exit the program? (y/n): ").lower()    # converts input to lowercase for consistency
    
    if response == "y":                                                     # if the user types 'y', exit the program
        print("Exiting the system... Goodbye")
        break
    
    elif response == "n":                                                   # if the user types 'n', continue the loop
        print("Continuing...")
    
    else:                                                                   # if the user types anything else, show an error message
        print("Invalid option, please try again")
