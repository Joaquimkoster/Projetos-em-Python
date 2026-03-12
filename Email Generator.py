import random                                                                                # allows you to use functions that generate random numbers or make random choices in Python

while True:                                                                                  # starts the loop
    print("===== Email Generator =====")                                                     # displays the title
    
                                                                                             # asks the user to enter the name or nickname they want to use, and converts it to lowercase, remove the spaces on the sides and in the middle
    name = input("Enter your Name or Nickname to use: ").lower().strip().replace(" ", "")
    
                                                                                             # defines the list of possible email domains
    domains = ["@gmail.com", "@hotmail.com", "@outlook.com",
               "@yahoo.com", "@live.com", "@icloud.com",
               "@aol.com", "@proton.me", "@protonmail.com",
               "@zoho.com", "@yandex.com", "@mail.com", "@gmx.com"]

                                                                                             # randomly selects one domain from the list
    chosen_domain = random.choice(domains)  
    
                                                                                             # combines the name and the chosen domain to form the email
    result = name + chosen_domain  
    
    print("Your new Email is", result)                                                       # displays the result
    
                                                                                             # asks the user if they want to exit
    while True:                                                                              # starts the loop
        exit_choice = input("Do you want to exit? (y/n): ").strip().lower()
    
        if exit_choice == "y":                                                               # if the user types 'y', completely terminates script execution.
           print("Exiting the program... Thank you for using it!!")
           exit()
    
        elif exit_choice == "n":                                                             # if the user types 'n', continue
           print("Continuing...")
           break
    
        else:                                                                                # if the user types anything else, display an invalid option message
            print("Invalid option, please try again") 