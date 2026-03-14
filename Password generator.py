import random                                                                # Imports the random library to generate random numbers and make random choices
import string                                                                # Imports the string library that contains useful strings like letters, digits, and symbols

while True:                                                                  # Starts an infinite loop that will be interrupted with a "break" command
    print("====== Password Generator ======")                                # Displays the title for the user
    
    try:
        char_count = int(input("Enter the number of characters: "))          # Converts the user's input into an integer
        
        if char_count <= 0:                                                  # Checks if the entered number is greater than 0
            print("Please enter a number greater than 0.")                   # If the number is 0 or negative, prompts for a new input
            continue                                                         # Returns to the start of the loop without proceeding with password generation

    except ValueError:                                                       # If the user enters something that is not a number
        print("Invalid input! Please enter a whole number (e.g., 8, 12, 16).")  # Displays an error message and goes back to the start of the loop
        continue                                                             # Returns to the start of the loop and asks for the number of characters again

    letters = string.ascii_letters                                           # Includes both uppercase and lowercase letters
    digits = string.digits                                                   # Includes numbers from 0 to 9
    symbols = string.punctuation                                             # Includes punctuation symbols like !, @, #, etc.

    all_characters = letters + digits + symbols                             # Combines all the strings into one

    password_list = random.choices(all_characters, k=char_count)             # Randomly selects the characters for the password
    password = "".join(password_list)                                        # Joins the generated characters into a single string

    print("\n")                                                              # Adds a blank line before displaying the password
    print("Your new password is:", password)                                 # Displays the generated password to the user
    
    response = input("Do you want to exit the program? (y/n): ").lower()     # Converts the response to lowercase

    if response == "y":                                                      # If the response is 'y', exit the program
        print("Exiting the system... Goodbye")
        break                                                                # Breaks the infinite loop and exits the program
    
    elif response == "n":                                                    # If the response is 'n', the program continues
        print("Continuing...\n")                                              # Displays a message informing that the program will continue
    
    else:                                                                    # If the response is neither 'y' nor 'n', displays an error message
        print("Invalid option, please try again.")                            # Informs that the input was invalid and continues the loop