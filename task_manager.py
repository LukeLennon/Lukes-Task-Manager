# Importing the relevant libraries which are needed for the project
import sys
from datetime import date

# Date required for the task part of this project
today = date.today()

# Opening the user text file to review what user's are in there
file_R = open("user.txt", "r")
is_user_loggedin = False
menu_option = ''
# Reading of the user text file we opened earlier
users = file_R.readlines()
# Below is a loop to be set and stay on False until the user has logged in
while (is_user_loggedin == False):

    # Input of the user's log in
    user_login = input("What is your username: ")
    # is user logged in needs to be kept at False to start, however when they eventually log in this will change, if
    # successful

    # User to insert their password
    user_pass = input("What is your password: ")

    # Looping through all the users and passwords in the user file
    for user in users:
        user_details = user.split(", ")  # Removal of the ", " to get just the username and password
        # Below is questioning if the details entered by the user are equal to
        # the 1st item on the list "[0]" (user login) and 2nd "[1]" (Password), if they match then the boolean which was
        # false will change to true
        if (user_details[0] == user_login) and (user_details[1].strip("\n") == user_pass):
            is_user_loggedin = True
            file_R.close()
            break  # Break is required as the loop will continue and will end the programme with the is_user_logged in with
            # false

    # Now the loop has breaked with is_user_logged in being True the programme will print you are logged in and continue
    if is_user_loggedin:
        print("\nYou are logged in, well done")
        # if the loop ended with a false, i.e. details did not match, the following message will appear and the programme
        # will end
    else:
        print("Details do not match the system, please try again.")

while menu_option != "e":

    # options below as per spec
    menu_text = '''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task \n'''
    # lower required incase user enters capitals

    if user_login == 'admin':
        menu_text += 'vs - View statistics \n'

    menu_text += 'e - Exit\n'

    menu_option = input(menu_text).lower()

    # Opening files no matter which option the user picks
    file_R = open("user.txt", "a")
    file_A = open("tasks.txt", "a")  # 'a' is used so that data can be appended, rather than overwritten
    file_VA = open("tasks.txt", "r+")
    file_VM = open("tasks.txt", "r+")

    # if user chooses r, the following details are asked for and written into the user file, ensuring that it does not
    # override
    if menu_option == 'r':
        if user_login == 'admin':
            username_R = input("Input an username: ")
            new_password_R = input("Input new password: ")
            confirm_password_R = input("Confirm password: ")
            if new_password_R == confirm_password_R:
                file_R.write(f"\n{username_R}, {new_password_R}")
            else:
                sys.exit("Error: Your password does not match, please start again")  # Error if password does not match
        else:
            print('Only the admin can register users, please choose another option')

    # Asking for input from client and to write into the task file in the correct format
    elif menu_option == 'a':
        username_A = input("Insert the username of the person the task is assigned to: ")
        title_A = input("Insert the title of the task: ")
        description_A = input("Insert a description of the task: ")
        duedate_A = input("Insert the due date of the task (YYYY-MM-DD): ")
        currentdate_A = today.strftime("%d %b %Y")
        file_A.write(f"\n{username_A}, {title_A}, {description_A}, {duedate_A}, {currentdate_A}, No")
        print((f"{username_A}, {title_A}, {description_A}, {duedate_A}, {currentdate_A}, No"))
        file_A.close()

    # below gets all the tasks in the task format and prints each one, using the loop function
    elif menu_option == 'va':
        lines_VA = file_VA.read()
        split_VA = lines_VA.split('\n')
        for index in split_VA:
            print(index)

    # below splits the tasks into lists, before being looped and split again so that each task is split up. This allows us
    # to check the username using the [0] placement. The programme widall print each task if it the username matches the [0]
    elif menu_option == "vm":
        lines_VM = file_VM.read()
        split_VM = lines_VM.split('\n')
        for items in split_VM:
            each_task = items.split(', ')
            if each_task[0] == user_login:
                print(each_task[1])

    elif menu_option == 'vs' and user_login == 'admin':
        tasks = file_VA.readlines()
        tasks_count = len(tasks)
        users_count = len(users)

        print('Amount of tasks: ' + str(tasks_count))
        print('Amount of users: ' + str(users_count))
        print("\n")

    elif menu_option == 'e':

        print('Goodbye!')
        exit()
    # if an option which is not in the list is typed in, the user will prompted to start again
    else:
        print("You have made a wrong choice, Please Try again")

