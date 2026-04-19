import json
import os

# No usarla como variable global
# to_do_list = {}


# Usar nombres descriptivos, load_file() no dice absolutamente nada
# El resultado se usa afuera por quien quiera
# Explicitar los tipos ayuda en los IDEs a los programadores
def load_to_do(file_path: str) -> dict:
    data = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try:
                data = json.load(f)

            except:
                print(f"WARN: Impossible to read input file: {file_path}")
                print()

    return data


# Usar nombres descriptivos, save_data() no dice nada, peor aún que data no refiere a todo's
def save_to_do(to_do: dict, file_path: str) -> None:
    with open(file_path, 'w') as f:
        json.dump(to_do, f, indent=2)


# No mezclar lo que dice la función con lo que hace -> agregar no es pedir los datos
# La acción se debe hacer sobre el objeto deseado, los diccionarios se pasan por referencia
def add_task(to_do: dict, task: str, description: str, priority: str, deadline: str) -> None:
    to_do[task] = {
        'Task': task,
        'Description': description,
        'Priority': priority,
        'Deadline': deadline
    }


# Hace una sola cosa
def get_task() -> tuple:
    task = input('Add a task to the list (Or write "Close" to close the todo list) ')
    if task.lower() == 'close':
        return None

    description = input('Add a description for the task (Write "None" to skip the description) ')
    if description.lower() == 'none':
        description = None

    priority = input('Add a priority for the task (High, Mid, Low) ')
    deadline = input('Enter the deadline for the task (YYYY/MM/DD) ')

    return task, description, priority, deadline


def fill_tasks(to_do: dict) -> None:
    while True:
        task_data = get_task()

        if task_data is None:
            break

        task = task_data[0]
        description = task_data[1]
        priority = task_data[2]
        deadline = task_data[3]

        add_task(to_do, task, description, priority, deadline)


# La forma de presentar cada tarea puede delegarse a otra función
def show_tasks(to_do: dict):
    if to_do:
        for key in to_do:
            print(to_do[key])
    else:
        print("The list is empty :/")


# Tarea para el hogar...
# Nombre de la función poco claro
def delete_task(to_do: dict):
    while True:
        task_to_delete = input("Select the task to delete (Or write 'Close' to exit): ")
        if task_to_delete.lower() == 'close':
            break

        elif task_to_delete in to_do:
            del to_do[task_to_delete]
            print(f"{task_to_delete} was deleted ;D")

        else:
            print("The item is not in the to do list, please check again.")


# Menu principal
# Mantengo el nombre to_do_list para facilitarte la comparación con el original
def menu():
    # No usar variables globales
    to_do_file_path = "to_do_list.json"

    to_do_list = load_to_do(to_do_file_path)

    while True:
        print("")
        print("1- Add task\n2- Show tasks\n3- Delete task\n4- Show options\n5- Exit")

        # input() siempre devuelve string, no es necesario convertirlo
        user_op = input("Choose an option (1/2/3/4/5): ")

        if user_op == '1':
            fill_tasks(to_do_list)
            save_to_do(to_do_list, to_do_file_path)

        elif user_op == '2':
            show_tasks(to_do_list)

        elif user_op == '3':
            delete_task(to_do_list)
            save_to_do(to_do_list, to_do_file_path)

        elif user_op == '4':
            # Nada que mostar, al inicio del bucle se presentan las opciones (evitar duplicados)
            pass

        elif user_op == '5':
            print("Closing the program")
            save_to_do(to_do_list, to_do_file_path)
            break

        else:
            print("Something went wrong. Please check again!")


if __name__ == "__main__":
    menu()
