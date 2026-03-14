import re                                                                      # imports the 're' module to use regular expressions
import string                                                                  # imports the string module that contains sets of characters
import sys                                                                     # imports sys to allow the program to exit safely


def validate_password(password):                                               # defines a function that will validate the password

    criteria = {                                                               # dictionary storing each validation rule and its result (True/False)
        "Minimum 8 characters": len(password) >= 8,                            # checks if password length is at least 8
        "At least one uppercase letter": bool(re.search(r"[A-Z]", password)),  # checks for at least one uppercase letter
        "At least one lowercase letter": bool(re.search(r"[a-z]", password)),  # checks for at least one lowercase letter
        "At least one number": bool(re.search(r"[0-9]", password)),            # checks for at least one digit
        "At least one special character": bool(re.search(rf"[{re.escape(string.punctuation)}]", password)),  # checks for special characters
    }

    points = sum(criteria.values())                                            # counts how many validation criteria were satisfied

    if points == 5:                                                            # if all criteria are satisfied
        level = "Strong Password "                                           # classifies password as strong
    elif 3 <= points < 5:                                                      # if 3 or 4 criteria are satisfied
        level = "Medium Password "                                           # classifies password as medium strength
    else:                                                                      # if fewer than 3 criteria are satisfied
        level = "Weak Password "                                             # classifies password as weak

    return criteria, level                                                     # returns the dictionary of criteria and the password strength level


while True:                                                                    # starts the main infinite loop of the program

    try:                                                                       # begins error handling block

        password = input("Enter a password to validate: ").strip()             # asks user to enter a password and removes extra spaces

        if not password:                                                       # checks if the user entered an empty password
            print("Password cannot be empty.\n")                                # informs the user that empty passwords are not allowed
            continue                                                           # restarts the loop asking for a new password

        criteria, level = validate_password(password)                          # calls the validation function and receives results

        print("\nValidation Result:\n")                                           # prints a title for the validation output

        for c, ok in criteria.items():                                         # loops through each validation rule and its result
            print(f"- {c}: {'OK' if ok else 'Failed'}")                         # prints whether each rule passed or failed

        print(f"\nLevel: {level}\n")                                            # prints the final password strength classification

        while True:                                                            # loop to ensure the user enters a valid exit option

            op = input("Do you want to exit? (y/n): ").strip().lower()          # asks user if they want to exit and normalizes input

            if op == "y":                                                      # if the user chooses to exit
                print("Exiting the system... Goodbye ")                       # prints exit message
                sys.exit()                                                      # safely terminates the program

            elif op == "n":                                                    # if the user chooses to continue
                print("Continuing...\n")                                        # prints continuation message
                break                                                           # exits this loop and returns to password validation

            else:                                                              # if user enters an invalid option
                print("Invalid option. Please type 'y' or 'n'.")                # informs the user and asks again

    except KeyboardInterrupt:                                                  # handles the case when the user presses CTRL + C
        print("\nProgram interrupted. Goodbye ")                              # prints interruption message
        sys.exit()                                                              # safely exits the program