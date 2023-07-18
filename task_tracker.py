import os

class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = "Incomplete"

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nPriority: {self.priority}\nStatus: {self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.file_name = "savedtasks.txt"

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

    def view_tasks(self):
        if self.tasks:
            for task in self.tasks:
                print(task)
                print('-' * 20)
        else:
            print("No tasks found.")

    def save_tasks(self):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            for task in self.tasks:
                file.write("Title: " + task.title + "\n")
                file.write("Description: " + task.description + "\n")
                file.write("Due Date: " + task.due_date + "\n")
                file.write("Priority: " + task.priority + "\n")
                file.write("Status: " + task.status + "\n")
                file.write('-' * 20 + '\n')


    def load_tasks_from_file(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r', encoding='utf-8', errors='replace') as file:
                task_data = file.read().split('\n' + '-' * 20 + '\n')
                for data in task_data:
                    if data:
                        task_info = data.split('\n')
                        task = Task(
                            self._extract_field_value(task_info[0], "Title"),
                            self._extract_field_value(task_info[1], "Description"),
                            self._extract_field_value(task_info[2], "Due Date"),
                            self._extract_field_value(task_info[3], "Priority")
                        )
                        task.status = self._extract_field_value(task_info[4], "Status")
                        self.add_task(task)

    def _extract_field_value(self, field_text, field_label):
        return field_text.split(field_label + ": ")[1]



if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.load_tasks_from_file()

    while True:
        print("Task Tracker")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date: ")
            priority = input("Enter task priority: ")

            task = Task(title, description, due_date, priority)
            task_manager.add_task(task)
            print("Task added successfully!")
            task_manager.save_tasks()

        elif choice == "2":
            task_manager.view_tasks()
            if task_manager.tasks:
                task_index = int(input("Enter the index of the task to delete: "))
                if 0 <= task_index < len(task_manager.tasks):
                    task_manager.delete_task(task_manager.tasks[task_index])
                    print("Task deleted successfully!")
                    task_manager.save_tasks()
                else:
                    print("Invalid task index.")

        elif choice == "3":
            print('\n')
            task_manager.view_tasks()
            print('\n')

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
