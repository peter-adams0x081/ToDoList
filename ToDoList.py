import Task


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        new_task = Task.Task(task_name)
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

            try:
                if choice == 1:
                    task_number = int(input("Enter the number of the task that you would like to rename: "))
                    new_name = input("Enter the new name for this task: ")
                    self.change_task_name((task_number - 1), new_name)
                elif choice == 2:
                    task_number = int(input("Enter the number of the task that you would like to remove: "))
                    self.remove_task(task_number - 1)
                elif choice == 3:
                    task_number = int(input("Enter the number of the task that you would like to mark completed: "))
                    self.tasks[task_number - 1].mark_completed()
                elif choice == 4:
                    return
                else:
                    print("Please enter a number shown in the task list menu options.")
            except ValueError:
                print("Please enter a valid integer for the task list menu.")

    def change_task_name(self, current_number, new_name):
        self.tasks[current_number].task_name = new_name

    def remove_task(self, task_number):
        self.tasks.remove(self.tasks[task_number])
