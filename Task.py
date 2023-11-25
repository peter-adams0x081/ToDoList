class Task:
    # TODO Task deadline
    def __init__(self, task_name):
        self.task_name = task_name
        self.completed = False

    def mark_completed(self):
        self.completed = True
