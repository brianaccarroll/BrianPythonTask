# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

# =====importing libraries===========
import os
from collections import defaultdict
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"


# Read task and user file function
def read_tasks():
    # Read tasks file if it is not created then create it first
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w"):
            pass
    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]
    tasks = []
    for t_str in task_data:
        curr_t = {}

        # Split by semicolon and manually add each component
        task_components = t_str.split(";")
        curr_t['username'] = task_components[0]
        curr_t['title'] = task_components[1]
        curr_t['description'] = task_components[2]
        curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[5] == "Yes" else False

        tasks.append(curr_t)

    return tasks


def read_user_file():
    # Read user file and if it does not exist create one
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")
    # Read in user_data
    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")

    username_password_dict = {}
    for user in user_data:
        username, password = user.split(';')
        username_password_dict[username] = password
    return username_password_dict


# Register a new user function. If the new user exists it will ask to choose another username.
def reg_user():
    # - Request input of a new username
    new_username = input("New Username: ")
    # Check if the new username already exists. If Yes, ask user to choose another username else
    # ask user to input password.
    if new_username in username_password.keys():
        print("Username already exists. Please choose another username.")
    else:
        # - Request input of a new password
        new_password = input("New Password: ")
        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")
        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password

            with open("user.txt", "w") as out_file:
                user_data_to_write = []
                for k in username_password:
                    user_data_to_write.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data_to_write))

        # - Otherwise you present a relevant message.
        else:
            print("Passwords do no match")


def add_task():
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file tasks.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    write_tasks()
    print("Task successfully added.")


def write_tasks():
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))


def view_all():
    # Pass a list of tasks to display_tasks function to display
    display_tasks(task_list)
    # Prompt user to choose a task to either mark or edit
    task_selection = int(input("Please choose a task: "))
    if task_selection != -1:
        task_menu = input('''Select one of the task operation below:
Mark - Mark a task
Edit - Adding a task
: ''').lower()
        if task_menu == "mark":
            # Mark the task to be completed and redisplay the task
            task_list[task_selection-1]['completed'] = True
            print(f"Task {task_selection} is marked.")
            write_tasks()
            display_tasks(task_list[task_selection-1])
        elif task_menu == "edit":
            # Edit the task to change username and due date. Cannot edit the task if it is completed
            if task_list[task_selection-1]['completed']:
                print("Cannot edit a completed task")
            else:
                changed_username = input("Please give a username to change: ")
                changed_due_date = input("Please give a due date to change (YYYY-MM-DD): ")
                changed_due_date = datetime.strptime(changed_due_date, DATETIME_STRING_FORMAT)
                task_list[task_selection-1]['username'] = changed_username
                task_list[task_selection-1]['due_date'] = changed_due_date
                write_tasks()
                display_tasks(task_list[task_selection-1])
    else:
        print("No task operation is selected.")


def display_tasks(tasks):
    """
        Display either a list of tasks or a specific task. If the input arguments is an instance
        of list, it display a list of tasks. Otherwise it display a specific task.
        Keyword arguments:
            tasks -- the list of tasks to display
    """
    if isinstance(tasks, list):
        task_number = 0
        for t in tasks:
            task_number += 1
            disp_str = f"{task_number}. ---------------------------------\n"
            disp_str += f"Task: \t\t\t  {t['title']}\n"
            disp_str += f"Assigned to: \t  {t['username']}\n"
            disp_str += f"Date Assigned: \t  {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t\t  {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: {t['description']}\n"
            complete_status = "Yes" if t['completed'] else "No"
            disp_str += f"Completed: \t\t  {complete_status}\n"
            print(disp_str)
    else:
        disp_str = f"Task: \t\t\t  {tasks['title']}\n"
        disp_str += f"Assigned to: \t  {tasks['username']}\n"
        disp_str += f"Date Assigned: \t  {tasks['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t\t  {tasks['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: {tasks['description']}\n"
        complete_status = "Yes" if tasks['completed'] else "No"
        disp_str += f"Completed: \t\t  {complete_status}\n"
        print(disp_str)


def view_mine():
    for t in task_list:
        if t['username'] == curr_user:
            # Call display_tasks function to display the task of mine
            display_tasks(t)


def generate_reports():
    total_tasks = len(task_list)
    # Dictionary to store the number of tasks per user, completed tasks and overdue tasks per user
    user_task_dict = defaultdict(int)
    user_completed_task_dict = defaultdict(int)
    user_overdue_task_dict = defaultdict(int)
    completed_tasks, overdue_tasks = 0, 0
    for t in task_list:
        if t['completed']:
            completed_tasks += 1
            # User completed task add 1
            user_completed_task_dict[t['username']] += 1
        elif t['due_date'] < datetime.today():
            overdue_tasks += 1
            # User overdue task add 1
            user_overdue_task_dict[t['username']] += 1
        # User task add 1
        user_task_dict[t['username']] += 1

    # Calculate task statistics
    uncompleted_tasks = total_tasks - completed_tasks
    uncompleted_percentage = uncompleted_tasks / total_tasks
    overdue_percentage = overdue_tasks / total_tasks

    # Write statistics to task overview report
    with open("task_overview.txt", "w") as task_overview_file:
        write_str = f"Total number of tasks: \t{total_tasks}\n"
        write_str += f"Completed tasks: \t{completed_tasks}\n"
        write_str += f"Uncompleted tasks: \t{uncompleted_tasks}\n"
        write_str += f"Overdue tasks: \t{overdue_tasks}\n"
        write_str += f"Uncompleted percentage is {uncompleted_percentage:.2%}\n"
        write_str += f"Overdue percentage is {overdue_percentage:.2%}"
        task_overview_file.write(write_str)

    # Write statistics to user overview report
    with open("user_overview.txt", "w") as user_overview_file:
        write_str = ""
        for k, v in user_task_dict.items():
            # Calculate user statistics
            user_task_percentage = v / total_tasks
            user_task_completion_percentage = user_completed_task_dict[k] / v
            user_task_uncompleted_percentage = (v-user_completed_task_dict[k]) / v
            user_task_overdue_percentage = user_overdue_task_dict[k] / v
            write_str += "--------------------------------------------------------------------\n"
            write_str += f"Total number of tasks assigned to {k}: \t{v}\n"
            write_str += f"Percentage of the tasks assigned to {k}: \t{user_task_percentage:.2%}\n"
            write_str += f"Percentage of the completed tasks that assigned to " \
                         f"{k}: \t{user_task_completion_percentage:.2%}\n"
            write_str += f"Percentage of the uncompleted tasks that assigned to " \
                         f"{k}: \t{user_task_uncompleted_percentage:.2%}\n"
            write_str += f"Percentage of the overdue tasks that assigned to " \
                         f"{k}: \t{user_task_overdue_percentage:.2%}\n"

        user_overview_file.write(write_str)


# Create tasks.txt if it doesn't exist before read
task_list = read_tasks()

# ====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account before read
username_password = read_user_file()

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        '''Call reg_user function to register a new user and add the new user to the user.txt file'''
        reg_user()

    elif menu == 'a':
        '''Call add_task function. Allow a user to add a new task to tasks.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
        add_task()

    elif menu == 'va':
        '''Call view_all function. Reads the task from tasks.txt file and prints to the console 
        in the format of Output 2 presented in the task pdf (i.e. includes spacing and labelling) '''
        view_all()

    elif menu == 'vm':
        '''Call view mine function. Reads the task from tasks.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing and labelling)'''
        view_mine()

    elif menu == 'gr' and curr_user == 'admin':
        '''Call generate reports function.'''
        generate_reports()

    elif menu == 'ds' and curr_user == 'admin':
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        username_password = read_user_file()
        task_list = read_tasks()
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")