import json
from task import Task

class TaskManager:
    def __init__(self, file_path="data/tasks.json"):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_path, "r") as file:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.file_path, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title):
        new_task = Task(title)
        self.tasks.append(new_task)
        self.save_tasks()

    def list_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "✔" if task.completed else "✘"
            print(f"{i}. {task.title} [{status}]")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
            