tasks = []                                              # creates the list 'tasks'
completed = []                                          # creates the list 'completed'

def add_tasks():                                        # creates the function add_tasks
    task = input("Enter Task: ")                        # defines the variable 'task' as what you type; input allows this
    tasks.append(task)                                  # adds the task to the 'tasks' list; append adds an item at the end of a list
    
def list_tasks():                                       # creates the function list_tasks
    print("\n--- Task List ---")                        # prints a text, \n creates a blank line above the text
    for i, t in enumerate(tasks):                       # goes through the 'tasks' list getting both the index (i) and the value (t)
        print(f"{i} - {t}")                             # f-string to print text together with variables. {} are replaced by variable values

def complete_tasks():                                   # creates the function complete_tasks
    for i, t in enumerate(tasks):                       # goes through the 'tasks' list getting both the index (i) and the value (t)
        print(f"{i} - {t}")                             # f-string prints text with variable values
        
    try: 
        num = int(input("Which task do you want to complete?: ")) # defines 'num' as what you type; int converts text to integer
        completed_task = tasks.pop(num)                # .pop(num) removes the item at index 'num' from 'tasks' and returns it; stored in 'completed_task'
        completed.append(completed_task)               # adds completed_task to the end of the 'completed' list
        print("Task completed!!")                      # prints a text

    except (ValueError, IndexError):
        print("Invalid index! Please try again.")

def delete_tasks():                                     # creates the function delete_tasks
    for i, t in enumerate(tasks):                       # goes through the 'tasks' list getting both the index (i) and the value (t)
        print(f"{i} - {t}")                             # f-string prints text with variable values

    try:
        num = int(input("Which task do you want to delete?: ")) # defines 'num' as what you type; int converts text to integer
        deleted_task = tasks.pop(num)                  # removes the item at position 'num' from the list 'tasks'; returns the removed item
        print(f"Task {deleted_task} deleted!")         # prints "Task X deleted!", where X is the removed task
    
    except (ValueError, IndexError):
        print("Invalid index! Please try again.")

while True:                                            # the code inside this while loop will run forever until you use a command to stop it
    print("\n")
    print("--- Task Manager ---")
    print("1. Add task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit program")

    op = input("Choose an option: ")                   # reads the option entered by the user
    print("\n")                                        # adds a blank line for organization

    if op == "1":                                      # if the user chose 1
        add_tasks()                                    # call the function to add tasks

    elif op == "2":                                    # if the user chose 2
        list_tasks()                                   # call the function to list tasks

    elif op == "3":                                    # if the user chose 3
        complete_tasks()                               # call the function to complete tasks

    elif op == "4":                                    # if the user chose 4
        delete_tasks()                                # call the function to delete tasks

    elif op == "5":                                    # if the user chose 5
        print("Exiting program...")                    # exit message
        break                                          # stops the while True loop

    else:                                              # if anything other than 1–5 is typed
        print("Invalid option!!")                      # informs it's invalid
        print(" ")                                     # adds a blank line