##import os
##
##class Task:
##    def __init__(self, title, description, due_date, priority):
##        self.title = title
##        self.description = description
##        self.due_date = due_date
##        self.priority = priority
##        self.status = "Incomplete"
##
##    def __str__(self):
##        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nPriority: {self.priority}\nStatus: {self.status}"
##
##    def complete_task(self):
##        self.status = "Complete"
##
##class TaskManager:
##    def __init__(self):
##        self.tasks = []
##        self.file_name = "savedtasks.txt"
##
##    def add_task(self, task):
##        self.tasks.append(task)
##
##    def delete_task(self, task):
##        self.tasks.remove(task)
##
##    def view_tasks(self):
##        if self.tasks:
##            for task in self.tasks:
##                print(task)
##                print('-' * 20)
##        else:
##            print("No tasks found.")
##
##    def complete_task(self):
##        self.view_tasks()
##        if self.tasks:
##            task_index = int(input("Enter the index of the task to mark as complete: "))
##            if 0 <= task_index < len(self.tasks):
##                task = self.tasks[task_index]
##                task.complete_task()
##                print("Task marked as complete.")
##                self.save_tasks()
##            else:
##                print("Invalid task index.")
##
##    def save_tasks(self):
##        with open(self.file_name, 'w', encoding='utf-8') as file:
##            for task in self.tasks:
##                file.write("Title: " + task.title + "\n")
##                file.write("Description: " + task.description + "\n")
##                file.write("Due Date: " + task.due_date + "\n")
##                file.write("Priority: " + task.priority + "\n")
##                file.write("Status: " + task.status + "\n")
##                file.write('-' * 20 + '\n')
##
##    def load_tasks_from_file(self):
##        if os.path.exists(self.file_name):
##            with open(self.file_name, 'r', encoding='utf-8', errors='replace') as file:
##                task_data = file.read().split('\n' + '-' * 20 + '\n')
##                for data in task_data:
##                    if data:
##                        task_info = data.split('\n')
##                        if len(task_info) >= 5:
##                            title = self._extract_field_value(task_info[0], "Title")
##                            description = self._extract_field_value(task_info[1], "Description")
##                            due_date = self._extract_field_value(task_info[2], "Due Date")
##                            priority = self._extract_field_value(task_info[3], "Priority")
##                            status = self._extract_field_value(task_info[4], "Status")
##                            task = Task(title, description, due_date, priority)
##                            task.status = status
##                            self.add_task(task)
##
##    def _extract_field_value(self, field_text, field_label):
##        return field_text.split(field_label + ": ")[1]
##
##
##if __name__ == "__main__":
##    task_manager = TaskManager()
##    task_manager.load_tasks_from_file()
##
##    while True:
##        print("Task Tracker")
##        print("1. Add Task")
##        print("2. Delete Task")
##        print("3. View Tasks")
##        print("4. Complete Task")
##        print("5. Exit")
##
##        choice = input("Enter your choice: ")
##
##        if choice == "1":
##            print('\n')
##            title = input("Enter task title: ")
##            description = input("Enter task description: ")
##            due_date = input("Enter task due date: ")
##            priority = input("Enter task priority: ")
##
##            task = Task(title, description, due_date, priority)
##            task_manager.add_task(task)
##            print("Task added successfully!")
##            task_manager.save_tasks()
##            print('\n')
##
##        elif choice == "2":
##            print('\n')
##            task_manager.view_tasks()
##            if task_manager.tasks:
##                task_index = int(input("Enter the index of the task to delete: "))
##                task_index -= 1
##                if 0 <= task_index < len(task_manager.tasks):
##                    task_manager.delete_task(task_manager.tasks[task_index])
##                    print("Task deleted successfully!")
##                    task_manager.save_tasks()
##                else:
##                    print("Invalid task index.")
##            print('\n')
##
##        elif choice == "3":
##            print('\n')
##            task_manager.view_tasks()
##            print('\n')
##
##        elif choice == "4":
##            print('\n')
##            task_manager.complete_task()
##            print('\n')
##
##        elif choice == "5":
##            print("Exiting...")
##            break
##
##        else:
##            print("Invalid choice. Please try again.")

import os
import json
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = "Incomplete"

    def __str__(self):
        formatted_due_date = self.due_date.strftime("%Y-%m-%d %H:%M")
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {formatted_due_date}\nPriority: {self.priority}\nStatus: {self.status}"

    def complete_task(self):
        self.status = "Complete"

    def is_completed(self):
        return self.status == "Complete"

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

    def create_task_from_user_input(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        due_date = self.get_valid_date_input("Enter task due date (YYYY-MM-DD): ")
        due_time = self.get_valid_time_input("Enter task due time (HH:MM): ")
        priority = input("Enter task priority: ")

        # Combine the date and time into a single datetime object
        due_datetime = datetime.combine(due_date.date(), due_time.time())

        return Task(title, description, due_datetime, priority)

    def get_valid_time_input(self, prompt):
        while True:
            time_input = input(prompt)
            try:
                due_time = datetime.strptime(time_input, "%H:%M")
                return due_time
            except ValueError:
                print("Invalid time format. Please use HH:MM.")

    def get_valid_date_input(self, prompt):
        while True:
            date_input = input(prompt)
            try:
                due_date = datetime.strptime(date_input, "%Y-%m-%d")
                return due_date
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    def delete_task(self):
        self.view_tasks()
        if self.tasks:
            task_index = self.get_valid_integer_input("Enter the index of the task to delete: ")
            if 1 <= task_index <= len(self.tasks):
                del_index = task_index - 1
                task = self.tasks[del_index]
                self.delete_task(task)
                print("Task deleted successfully!")
                self.save_tasks()
            else:
                print("Invalid task index.")

    def complete_task(self):
        self.view_tasks()
        if self.tasks:
            task_index = self.get_valid_integer_input("Enter the index of the task to mark as complete: ")
            if 1 <= task_index <= len(self.tasks):
                task = self.tasks[task_index - 1]
                if task.is_completed():
                    print("This task is already marked as complete.")
                else:
                    task.complete_task()
                    print("Task marked as complete.")
                    self.save_tasks()
            else:
                print("Invalid task index.")

    def save_tasks(self):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            serialized_tasks = []
            for task in self.tasks:
                serialized_task = {
                    "title": task.title,
                    "description": task.description,
                    "due_date": task.due_date.strftime("%Y-%m-%d %H:%M"),
                    "priority": task.priority,
                    "status": task.status
                }
                serialized_tasks.append(serialized_task)
            json.dump(serialized_tasks, file, indent=2)

    def load_tasks_from_file(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r', encoding='utf-8', errors='replace') as file:
                try:
                    serialized_tasks = json.load(file)
                except json.JSONDecodeError:
                    print("Error loading tasks from file.")
                    return
                for serialized_task in serialized_tasks:
                    title = serialized_task.get("title")
                    description = serialized_task.get("description")
                    due_date_str = serialized_task.get("due_date")
                    priority = serialized_task.get("priority")
                    status = serialized_task.get("status")

                    try:
                        due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
                    except ValueError:
                        # If there's an error in parsing the datetime, try parsing only the date
                        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")

                    task = Task(title, description, due_date, priority)
                    task.status = status
                    self.add_task(task)


if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.load_tasks_from_file()

    while True:
        print("Task Tracker")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Complete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print()
            task = task_manager.create_task_from_user_input()
            task_manager.add_task(task)
            print("Task added successfully!")
            task_manager.save_tasks()
            print()

        elif choice == "2":
            print('\n')
            task_manager.delete_task()
            print('\n')

        elif choice == "3":
            print('\n')
            task_manager.view_tasks()
            print('\n')

        elif choice == "4":
            print('\n')
            task_manager.complete_task()
            print('\n')

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
