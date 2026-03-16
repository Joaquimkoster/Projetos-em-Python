tasks = []                                                                                # Creates an empty list to store pending tasks
completed = []                                                                            # Creates an empty list to store finished tasks

def list_tasks_helper():                                                                  # Defines a helper function to avoid repeating code when listing tasks
    if not tasks:                                                                         # Checks if the 'tasks' list is empty
        print("Your task list is empty!")                                                 # Displays a message if there are no tasks to show
        return False                                                                      # Returns False to indicate the list has no items
    for i, t in enumerate(tasks):                                                         # Loops through the 'tasks' list getting index (i) and content (t)
        print(f"{i} - {t}")                                                               # Displays the formatted index next to the task name
    return True                                                                           # Returns True indicating the list has items and was displayed

def add_tasks():                                                                          # Defines the function to add new tasks
    task = input("Enter Task: ").strip()                                                  # Gets input and .strip() removes useless spaces at start/end
    if task:                                                                              # Checks if the task is not an empty string
        tasks.append(task)                                                                # Adds the typed task to the end of the 'tasks' list
        print(f"Task '{task}' added!")                                                    # Confirms to the user that the task was saved
    else:                                                                                 # If the user just pressed Enter without typing anything
        print("Error: The task cannot be empty.")                                         # Displays an error message

def list_tasks():                                                                         # Defines the function to display the listing interface
    print("\n--- Task List ---")                                                          # Prints the task list header
    if not list_tasks_helper():                                                           # Calls the helper function and checks if it returned False
        pass                                                                              # If empty, does nothing extra (helper already warned user)

def show_completed():                                                                     # Defines the function to view finished tasks
    print("\n--- Tasks Already Completed ---")                                            # Prints the completed tasks header
    if not completed:                                                                     # Checks if the 'completed' list is empty
        print("No tasks completed yet.")                                                  # Informs that there is no completion history yet
    for t in completed:                                                                   # Loops through each item inside the completed list
        print(f"[X] {t}")                                                                 # Displays the task with a checkmark [X]

def complete_tasks():                                                                     # Defines the function to mark a task as done
    print("\n--- Complete a Task ---")                                                    # Prints the action header
    if list_tasks_helper():                                                               # Only proceeds if the helper function finds pending tasks
        try:                                                                              # Starts an error handling block (for letters or wrong indices)
            num = int(input("Which task do you want to complete?: "))                     # Converts user input into an integer
            completed_task = tasks.pop(num)                                               # Removes task from 'tasks' list and stores it in a variable
            completed.append(completed_task)                                              # Moves that task to the 'completed' list
            print(f"Task '{completed_task}' marked as completed!!")                       # Confirms completion to the user
        except (ValueError, IndexError):                                                  # Catches typing errors (letters) or numbers out of range
            print("Invalid index! Please enter a valid number from the list.")            # Warns that the input was invalid

def delete_tasks():                                                                       # Defines the function to permanently delete a task
    print("\n--- Delete a Task ---")                                                      # Prints the action header
    if list_tasks_helper():                                                               # Checks if there are tasks to be deleted
        try:                                                                              # Starts error handling for the user input
            num = int(input("Which task do you want to delete?: "))                        # Converts user input into an integer
            deleted_task = tasks.pop(num)                                                 # Removes the task from the list without moving it elsewhere
            print(f"Task '{deleted_task}' deleted!")                                      # Confirms the deletion of the task
        except (ValueError, IndexError):                                                  # Catches value errors (letters) or non-existent indices
            print("Invalid index! Please try again.")                                     # Warns that the input was invalid

while True:                                                                               # Starts an infinite loop to keep the program running
    print("\n" + "="*20)                                                                  # Prints a decorative separator line
    print("--- Task Manager ---")                                                         # Displays the main menu title
    print("1. Add task")                                                                  # Option 1: Add
    print("2. List pending tasks")                                                        # Option 2: List pending
    print("3. Complete task")                                                             # Option 3: Complete
    print("4. Delete task")                                                               # Option 4: Delete
    print("5. View completed tasks")                                                      # Option 5: View completed
    print("6. Exit program")                                                              # Option 6: Exit
    print("="*20)                                                                         # Prints another decorative line

    op = input("Choose an option: ")                                                      # Captures the user's choice
    print("\n")                                                                           # Jumps a line to organize the visual layout

    if op == "1":                                                                         # If choice is "1"
        add_tasks()                                                                       # Calls the add function
    elif op == "2":                                                                       # If choice is "2"
        list_tasks()                                                                      # Calls the pending list function
    elif op == "3":                                                                       # If choice is "3"
        complete_tasks()                                                                  # Calls the complete function
    elif op == "4":                                                                       # If choice is "4"
        delete_tasks()                                                                    # Calls the delete function
    elif op == "5":                                                                       # If choice is "5"
        show_completed()                                                                  # Calls the show completed function
    elif op == "6":                                                                       # If choice is "6"
        print("Exiting program... Goodbye!")                                              # Displays a farewell message
        break                                                                             # Breaks the 'while True' loop and closes the program
    else:                                                                                 # If the user types anything else
        print("Invalid option!! Please choose between 1 and 6.")                          # Informs that the option is invalid