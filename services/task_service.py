

# this file:
#business logic
# interact w/ TaskModel (database layer).
# Perform task operations such a filtering by category, priority, or due date. 
# Ensure data validations before inserting into the database.
from colorama import Fore, Style, init
from models.task_model import TaskModel

class TaskService:
    def __init__(self, db_name = "tasks.db"):
        self.task_model = TaskModel(db_name)
        
    def add_task(self, title, description, category, priority, due_date):
        if not title or priority not in ('low', 'medium', 'high'):
            raise ValueError("Invalid title or priority")
        return self.task_model.add_task(title, description, category, priority, due_date)
    
    def get_all_tasks(self):
        tasks = self.task_model.get_all_tasks()
        return [self._format_task(task) for task in tasks]
    
    def get_tasks_by_category(self, category):
        category = category.lower().strip()
        tasks = self.get_all_tasks()
        return [task for task in tasks if task.get("Category", "").lower().strip() == category]
    
    def get_tasks_by_priority(self, priority):
        priority = priority.lower().strip()
        valid_priorities = {"low", "medium", "high"}
        if priority not in valid_priorities:
            print(Fore.RED + "Error: Please enter a valid input (Low/Medium/High).")
            return []
        tasks = self.get_all_tasks()
        filtered_tasks = [task for task in tasks if task.get("Priority", "").strip().lower() == priority]
        return filtered_tasks
    
    def mark_task_completed(self, task_id):
        return self.task_model.update_task_status(task_id, 'Completed')
    
    def delete_task(self, task_id):
        return self.task_model.delete_task(task_id)
    
    def _format_task(self, task):
        return {
            "ID": task["id"],
            "Title": task["title"],
            "Description": task["description"],
            "Category": task["category"],
            "Priority": task["priority"],
            "Due Date": task["due_date"],
            "Completed": task["status"]
        }
