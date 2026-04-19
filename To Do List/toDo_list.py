import json
import os

to_do_list = {}

file_path = "to_do_list.txt"

#Open and load the json file
def load_file(file_path):
    global to_do_list
    if os.path.exists(file_path):
        with open(file_path, 'r') as ToDoList:
            for key, value in to_do_list.items():
                ToDoList.write(f"{key}: {value}\n")
    else:
        to_do_list = {}

#Save the dictionary in a json file
def save_data(file_path):
    with open(file_path, 'w') as ToDoList:
        json.dump(to_do_list, ToDoList, indent=2)

#Add a taks to the to do list
def add_task():
    while True:
        task = input('Add a task to the list (Or write "Close" to close the todo list) ')
        if task.lower() == 'close':
            break
        description = input('Add a description for the task (Write "None" to skip the description) ')
        if description.lower() == 'none':
            description = None 
        priority = input('Add a priority for the task (High, Mid, Low) ')
        deadline = input('Enter the deadline for the task (YYYY/MM/DD) ')
        #Add the dictionary to the to do list
        to_do_list[task] = {
            'Task': task,
            'Description': description,
            'Priority': priority,
            'Deadline': deadline,
        }

#This function itared the list of taks and show them in the console
def show_tasks():
    if not to_do_list:
        print("The list is empty :/")
    else:
        for task in to_do_list:
            print(to_do_list[task])

#The function iterated through the tasks in 'to_do_list' until it found the task entered by the user.
def delete_task():
    while True:
        task_to_delete = input("Select the task to delete (Or write 'Close' to exit): ")
        if task_to_delete.lower() == 'close':
            break
        elif task_to_delete in to_do_list:
            del to_do_list[task_to_delete]
            print(f"{task_to_delete} was delete succesfully ;D")
        else:
            print("The item is not in the to do list, please check again.")
#It's just a menu bruh
def menu():
    load_file(file_path)

    while True:
        print("1- Add task\n2- Show tasks\n3- Delete task\n4- Show options\n5- Exit")
        user_op = str(input("Choose an option (1/2/3/4/5): "))
        if user_op == '1':
            add_task()
            save_data(file_path)
        elif user_op == '2':
            show_tasks()
        elif user_op == '3':
            delete_task()
            save_data(file_path)
        elif user_op == '4':
            print("1- Add task\n2- Show tasks\n3- Delete task\n4- Show this menu\n5- Exit")
        elif user_op == '5':
            print("Closing the program")
            save_data(file_path)
            break
        else:
            print("Something went wrong. Please check again")

menu()