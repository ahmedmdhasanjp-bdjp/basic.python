class Task:
    next_id = 1

    def __init__(self, title, due_date=None):
        self.task_id = Task.next_id
        Task.next_id += 1

        self.title = title
        self.status = "Pending"
        self.due_date = due_date

    def __str__(self):
        return f"ID: {self.task_id}, Title: {self.title}, Status: {self.status}, Due Date: {self.due_date}"
class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, title, due_date=None):
        task = Task(title, due_date)
        self.tasks.append(task)
        print("Task added successfully.")

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def search_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                print(task)
                return
        print("Task not found.")
