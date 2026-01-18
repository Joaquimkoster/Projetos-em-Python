import re                                                     # imports the 're' module to use regular expressions

def validate_password(password):                              # creates the function 'validate_password'
    
    
    criteria = {
        "length": len(password) >= 8,                         # checks if password has at least 8 characters
        "uppercase": bool(re.search(r"[A-Z]", password)),     # checks if password has at least one uppercase letter
        "lowercase": bool(re.search(r"[a-z]", password)),     # checks if password has at least one lowercase letter
        "number": bool(re.search(r"[0-9]", password)),        # checks if password has at least one number
        "special": bool(re.search(r"[@#$%!&*?]", password)),  # checks if password has at least one special character
    }

    points = sum(criteria.values())                           # counts how many criteria were met (True counts as 1)

   
    if points == 5:                                           # if all criteria are met
        level = "Strong Password 🔥"
    elif 3 <= points < 5:                                     # if 3 or 4 criteria are met
        level = "Medium Password ⚠️"
    else:                                                     # if less than 3 criteria are met
        level = "Weak Password ❌"

    return criteria, level                                    # returns the criteria dictionary and the strength level


password = input("Enter a password to validate: ")            # asks the user to input a password

criteria, level = validate_password(password)                 # calls the function to validate the password

print("\nValidation Result:")                                 # prints the result title
for c, ok in criteria.items():                                # loops through each criterion and its result
    print(f"- {c}: {'OK' if ok else 'Failed'}")               # prints whether each criterion was met

print(f"\nLevel: {level}")                                    # prints the overall password strength
