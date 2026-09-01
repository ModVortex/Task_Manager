#=====importing libraries===========
from datetime import date


def load_users():
    """
    This function loads the users from the user.txt file and returns two lists:
    one for usernames and one for passwords.
    """
    usernames = []
    passwords = []
    with open('user.txt', 'r') as f:
        for line in f:
            username, password = line.strip().split(", ")
            usernames.append(username)
            passwords.append(password)
    return usernames, passwords

def login(usernames, passwords):
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in usernames:
            password_index = usernames.index(username)

            if password == passwords[password_index]:
                print("Login successful")
                return username

            print("Incorrect password.")

        else:
            print("Username does not exist.")


def register_user():
    new_username = input("Enter the new user's username: ")
    new_password = input("Enter the new user's password: ")
    confirm_password = input("Confirm the new user's password: ")

    if new_password == confirm_password:
        with open('user.txt', 'a') as f:
            f.write(f"{new_username}, {new_password}\n")
        print("Registration successful!")
    else:
        print("Passwords do not match. Registration failed.")

def add_task():
    """
    Add tasks to users
    """

    task_username = input("Enter the username of the person who the task is for: ")
    task_title = input("Enter the task title: ")
    task_description = input("Enter the task description: ")
    task_due_date = input("Enter the task due date (YYYY-MM-DD): ")
    current_date = date.today().strftime("%Y-%m-%d")

    with open("tasks.txt", "a") as f:
        f.write(
            f"{task_username}, {task_title}, {task_description}, "
            f"{current_date}, {task_due_date}, No\n"
        )
    print("Task added successfully.")



def view_all_tasks():
    """
    Shows all tasks
    """
    with open("tasks.txt", "r") as f:
        for line in f:
            task_details = line.strip().split(", ")
            print(f"Task:            \t{task_details[1]}")
            print(f"Assigned to:     \t{task_details[0]}")
            print(f"Date assigned:   \t{task_details[3]}")
            print(f"Due Date:        \t{task_details[4]}")
            print(f"Task Complete?   \t{task_details[5]}")
            print(f"Task description:\t")
            print(f" {task_details[2]}")

def view_my_tasks(username):
    """
   Shows the user his/her tasks
    """
    with open("tasks.txt", "r") as f:
        for line in f:
            task_details = line.strip().split(", ")
            if task_details[0] == username:
                print(f"Task:            \t{task_details[1]}")
                print(f"Assigned to:     \t{task_details[0]}")
                print(f"Date assigned:   \t{task_details[3]}")
                print(f"Due Date:        \t{task_details[4]}")
                print(f"Task Complete?   \t{task_details[5]}")
                print(f"Task description:\t")
                print(f" {task_details[2]}")

def display_statistics():
    """
    Display statistics about tasks and users
    """
    f = open("tasks.txt", 'r+')
    total_tasks = 0
    for lines in f:
        total_tasks += 1
    f.close()

    f = open("user.txt", 'r+') 
    total_users = 0 
    for lines in f:
        total_users += 1           
    f.close()   

    print(f"Total Tasks:\t{total_tasks}")
    print(f"Total Users:\t{total_users}")  

def complete_task(username, task_title):
    """
    Marks the specified task as complete for the logged-in user.
    """
    with open("tasks.txt", "r") as f:
        lines = f.readlines()

    with open("tasks.txt", "w") as f:
        for line in lines:
            task_details = line.strip().split(", ")
            if task_details[1] == task_title and task_details[0] == username:
                task_details[5] = "Yes"
                print(f"Task '{task_title}' marked as complete.")
            f.write(", ".join(task_details) + "\n")

usernames, passwords = load_users()
username = login(usernames, passwords)

while True:
    menu = input('''
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my tasks
st - View statistics
c - Complete task   
e - Exit
: ''').lower()

    if menu == "r":
        if username == "admin":
            register_user()
        else:
            print("You are not allowed to register new users.")

    elif menu == "a":
        add_task()

    elif menu == "va":
        view_all_tasks()

    elif menu == "vm":
        view_my_tasks(username)

    elif menu == "st":
        display_statistics()

    elif menu == "c":
        task_title = input("Enter the title of the task you want to mark as complete: ")
        complete_task(username, task_title)

    elif menu == "e":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")




    
