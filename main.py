import sys
import Task
import ToDoList
import tkinter as tk

"""
TODO: Create menu options function for view task list option. 
        -Modify a task deadline. 
            -Import datetime.
            -Use a timedelta to determine time remaining b4 deadline
                -Subtract current d/t from deadline d/t, returning a timedelta representing remaining time b4 deadline
TODO: Implement File I/O.
TODO: Import tkinter library (import tkinter as tk) to create GUI.
        -This will allow more robust features like task descriptions, hover options, etc.
TODO: Implement aware D/T's using pytz.
"""


def show_main_menu(to_do_list):
    while True:
        print("\nMenu options:")
        print("1. View task list.")
        print("2. Add a new task.")
        print("3. Exit program.")
        choice = input("Enter the number for your choice: ")
        try:
            if choice == "1":
                to_do_list.display_tasks()
            elif choice == "2":
                task_name = input("Enter a name for the task you would like to add: ")
                to_do_list.add_task(task_name)
            elif choice == "3":
                print("\nExiting program. Let's get a good start on your tasks for today!", end="")
                sys.exit()
            else:
                print("Please enter a number shown in the main menu options.")
        except ValueError:
            print("Please enter a valid integer for the main menu.")


def main():
    to_do = ToDoList.ToDoList()

    print("\nWelcome to your task manager.")

    show_main_menu(to_do)


if __name__ == '__main__':
    main()
