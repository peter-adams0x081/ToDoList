import sys, datetime, pytz

"""
TODO: Create menu options function for view task list option. 
        -Modify a task name.
        -Modify a task deadline. 
            -Import datetime.
            -Use a timedelta to determine time remaining b4 deadline
                -Subtract current d/t from deadline d/t, returning a timedelta representing remaining time b4 deadline
        -Remove a task from your queue.
TODO: Implement File I/O.
TODO: Import tkinter library (import tkinter as tk) to create GUI.
        -This will allow more robust features like task descriptions, hover options, etc.
TODO: Implement aware D/T's using pytz.
"""


class Task:
    # TODO Task deadline
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
        while True:
            # TODO Display task deadline
            print("\nTasks in queue:")
            print("---------------")
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task.completed else "Incomplete"
                print(f"{idx}. {task.task_name} - {status}")
            print("---------------")

            print("\nMenu Options:")
            print("1. Modify a task name.")
            print("2. Remove a task.")
            print("3. Mark a task as completed.")
            print("4. Return to main menu.")

            choice = int(input("Enter a number corresponding to a menu option: "))

            if choice == 1:
                task_number = int(input("Enter the number of the task that you would like to rename: "))
                new_name = input("Enter the new name for this task: ")
                self.change_task_name(task_number, new_name)
            elif choice == 2:
                task_number = int(input("Enter the number of the task that you would like to remove: "))
                self.remove_task(task_number)
            elif choice == 3:
                task_number = int(input("Enter the number of the task that you would like to mark completed: "))
                self.tasks[task_number].mark_complete()
            elif choice == 4:
                return
            else:
                print("Please enter a number corresponding to a menu option.")

    def change_task_name(self, current_number, new_name):
        self.tasks[current_number - 1] = new_name

    def remove_task(self, task_number):
        self.tasks.remove(task_number)


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
