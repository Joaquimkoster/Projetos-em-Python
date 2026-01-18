def register():                                                  # creates the function 'register'
    
    print("")                                                    # creates an empty line
    print("=== USER REGISTRATION ===")                           # displays the text
    username = input("Enter your username: ")                    # sets 'username' as what you type
    password = input("Enter your password: ")                    # sets 'password' as what you type

    with open("Registration.txt", "w") as file:                  # opens 'Registration.txt' in "w" (write) mode. ERASES everything that existed before. Creates the file if it doesn't exist. 'with' closes the file automatically.
        file.write(f"{username},{password}\n")                   # writes username and password separated by a comma
    
    print("Registration saved successfully!!!")                  # displays the text

def login():                                                     # creates the function 'login'
    
    print("")                                                    # creates an empty line
    print("=== USER LOGIN ===")                                  # displays the text
    username = input("Enter your username: ")                    # sets 'username' as what you type
    password = input("Enter your password: ")                    # sets 'password' as what you type
    
    with open("Registration.txt", "r") as file:                  # opens the file in "r" (read) mode. Reads all content into the variable 'content'
        content = file.read()

    if username in content:                                      # if username is in content, prints a message
        print("User logged in successfully!!!")
    else:                                                        # otherwise, prints another message
        print("User not found, please try again")

    if password in content:                                      # if password is in content, prints a message
        print("Password verified successfully!!!")
    else:                                                        # otherwise, prints another message
        print("Password not found, please try again")


while True:                                                       # loop that runs indefinitely
    
    print("")                                                     # prints an empty line
    print("===== System =====")                                   # displays a text
    print("1) Register")                                          # displays a text
    print("2) Login")                                             # displays a text
    print("3) Exit")                                              # displays a text

    option = input("Choose an option: ")                          # sets 'option' as what you type

    if option == "1":                                             # if option is 1, call and execute 'register'
        register()
    elif option == "2":                                           # otherwise, if option is 2, call and execute 'login'
        login()
    elif option == "3":                                           # otherwise, if option is 3, exit the program, break the loop
        print("Exiting the system...")
        break
    else:                                                         # otherwise, prints a message
        print("Invalid option, please try again")
