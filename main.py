import sys

"""
TODO: Create menu options function for view task list option. 
        -Modify a task name.
        -Modify a task deadline. 
        -Remove a task from your queue.
TODO: Implement File I/O.
        -bin location?
TODO: Import tkinter library (import tkinter as tk) to create GUI.
        -This will allow more robust features like task descriptions, hover options, etc.
"""


class Task:
    # TODO Task deadline
    # Implement date-time feature? maybe too advanced. try it out.
    def __init__(self, task_name):
        self.task_name = task_name
        self.completed = False

    def mark_completed(self):
        self.completed = True


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        new_task = Task(task_name)
        self.tasks.append(new_task)

    def display_tasks(self):
        # TODO Display task deadline
        print("\nTasks in queue:")
        print("---------------")
        for idx, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Incomplete"
            print(f"{idx}. {task.task_name} - {status}")
        print("---------------")

    def remove_task(self, task_name):
        self.tasks.remove(task_name)


def show_main_menu(to_do_list):
    while True:
        print("\nMenu options:")
        print("1. View task list.")
        print("2. Add a new task.")
        print("3. Exit program.")
        choice = input("Enter the number for your choice: ")

        if choice == "1":
            to_do_list.display_tasks()
        elif choice == "2":
            task_name = input("Enter a name for the task you would like to add: ")
            to_do_list.add_task(task_name)
        elif choice == "3":
            print("\nExiting program. Let's get a good start on your tasks for today!", end="")
            sys.exit()
        else:
            print("Please enter a valid number corresponding to one of the menu options.")


def main():
    to_do = ToDoList()

    print("\nWelcome to your task manager.")

    show_main_menu(to_do)


if __name__ == '__main__':
    main()
