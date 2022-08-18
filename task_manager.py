'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

#=====importing libraries===========
from datetime import date

#====Login Section====
"""
Here I do the following
1) Make 2 lists -> one for the username and one for passwords
2) Then I store the textfiles contents in a variable 
3) Then I put the username and password in the textfile in the 2 lists
4) Then I use a while loop to validate the login of the user
5) When the user enters an incorrect username or password
   1: I will ask them if they want to try again
   2: If they input "y" they can try again
   3: If they input "n" the program will close
   4: The reason I do this is because if the user cant remember their login details
      they wont be stuck in an infinite loop where they ask the user for the login details
6) If the user enters the correct login details the program will print: Login successful 
"""
today = date.today()
list_Usernames = []
list_Passwords = []
f = open('user.txt','r+')
for lines in f:
    line = lines.split(", ")
    list_Usernames.append(line[0]) 
    list_Passwords.append(line[1]) 
f.close()
while True:
    username, password = input("Enter your username:\t"), input("Enter your password:\t")
    if username in list_Usernames:
        password_index = list_Usernames.index(username) 
        if password == list_Passwords[password_index]:
            print("Login successful")
            break
        else:
            print("Your password is incorrect.")
            while True:
                prompt_answer = input("Do you want to try again to login? [y/n]: ")
                if prompt_answer.lower() == "y":
                    break
                elif prompt_answer.lower() == "n":
                    exit()
                else:
                    print("Wrong input. Only y or n allowed")
                    continue
            continue
    else:
        print("The username does not exist")
        while True:
                prompt_answer = input("Do you want to try again to login? [y/n]: ")
                if prompt_answer.lower() == "y":
                    break
                elif prompt_answer.lower() == "n":
                    exit()
                else:
                    print("Wrong input. Only 'y' or 'n' allowed")
                    continue
        continue    

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if username == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
        
        if menu == 'r':
            #Registration of new users
            """
            This is the code used for registering a new user
            """
            if username == "admin":
                new_username = input("Enter the new users username:\t")
                new_password = input("Enter the new users password:\t")
                if new_password == input("Confirm new users password:\t"):
                    f = open('user.txt', 'r+')
                    f.write(f"{new_username}, {new_password}")
                    f.close()
                    print("Registration successful!")
                else:
                    print("The password you entered is not the same as the one u entered first")
            else:
                print("You are not allowed to register new users.")
            
            

        elif menu == 'a':
            #Task registration
            """
            This code is used to give users tasks and put them in the tasks.txt file
            """
            task_username = input("Enter the username of the person who the task is for: ")
            task_title = input("Enter the task title: ")
            task_description = input("Enter the task desciption: ")
            task_dueDate = input("Enter the task due date: ")
            current_date = today.strftime("%d %b %y")
            print(current_date)
            f = open("tasks.txt", "r+")
            f.write(f"{task_username}, {task_title}, {task_description}, {current_date}, {task_dueDate}, No")
            f.close()

        elif menu == 'va':
            #View of all tasks
            """
            This code is used to show all tasks
            """
            f = open("tasks.txt", "r+")
            for lines in f:
                line = lines.split(", ") 
                print(f"Task:            \t{line[1]}")
                print(f"Assigned to:     \t{line[0]}")
                print(f"Date assigned:   \t{line[3]}")
                print(f"Due Date:        \t{line[4]}")
                print(f"Task Complete?   \t{line[5]}")
                print(f"Task description:\t")
                print(f" {line[2]}")
            f.close()

        elif menu == 'vm':
            #View of my tasks
            """
            This code is used to show the user his/her tasks
            """
            f = open("tasks.txt", "r+")
            for lines in f:
                line = lines.split(", ") 
                if line[0] == username:
                    print(f"Task:            \t{line[1]}")
                    print(f"Assigned to:     \t{line[0]}")
                    print(f"Date assigned:   \t{line[3]}")
                    print(f"Due Date:        \t{line[4]}")
                    print(f"Task Complete?   \t{line[5]}")
                    print(f"Task description:\t")
                    print(f" {line[2]}")
            f.close()
        
        elif menu == 'st':
            #View of all tasks and users
            """
            This code is used to show the total tasks and users
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

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")
    
    
    
    
    else:
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
    
    if menu == 'r':
        #Registration of new users
        """
        This is the code used for registering a new user
        """
        if username == "admin":
            new_username = input("Enter the new users username:\t")
            new_password = input("Enter the new users password:\t")
            if new_password == input("Confirm new users password:\t"):
                f = open('user.txt', 'r+')
                f.write(f"{new_username}, {new_password}")
                f.close()
                print("Registration successful!")
            else:
                print("The password you entered is not the same as the one u entered first")
        else:
            print("You are not allowed to register new users.")
        
        

    elif menu == 'a':
        #Task registration
        """
        This code is used to give users tasks and put them in the tasks.txt file
        """
        task_username = input("Enter the username of the person who the task is for: ")
        task_title = input("Enter the task title: ")
        task_description = input("Enter the task desciption")
        task_dueDate = input("Enter the task due date")
        current_date = today.strftime("%d %b %y")
        print(current_date)
        f = open("tasks.txt", "r+")
        f.write(f"{task_username}, {task_title}, {task_description}, {current_date}, {task_dueDate}, No")
        f.close()

    elif menu == 'va':
        #View of all tasks
        """
        This code is used to show all tasks
        """
        f = open("tasks.txt", "r+")
        for lines in f:
            line = lines.split(", ") 
            print(f"Task:            \t{line[1]}")
            print(f"Assigned to:     \t{line[0]}")
            print(f"Date assigned:   \t{line[3]}")
            print(f"Due Date:        \t{line[4]}")
            print(f"Task Complete?   \t{line[5]}")
            print(f"Task description:\t")
            print(f" {line[2]}")
        f.close()

    elif menu == 'vm':
        #View of my tasks
        """
        This code is used to show the user his/her tasks
        """
        f = open("tasks.txt", "r+")
        for lines in f:
            line = lines.split(", ") 
            if line[0] == username:
                print(f"Task:            \t{line[1]}")
                print(f"Assigned to:     \t{line[0]}")
                print(f"Date assigned:   \t{line[3]}")
                print(f"Due Date:        \t{line[4]}")
                print(f"Task Complete?   \t{line[5]}")
                print(f"Task description:\t")
                print(f" {line[2]}")
        f.close()
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")




    