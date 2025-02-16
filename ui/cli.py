# handles user interaction
import sys
import os
import sqlite3
import argparse
from services.task_service import TaskService

def main():
    task_service = TaskService()
    parser = argparse.ArgumentParser(description="Task Management CLI")
    
    parser.add_argument("--add", nargs=4, metavar=("TITLE", "DESCRIPTION", "CATEGORY", "PRIORITY"), 
                        help="Add a new task")
    parser.add_argument("--list", action="store_true", help="List all tasks")
    parser.add_argument("--filter-category", metavar="CATEGORY", help="Filter tasks by category")
    parser.add_argument("--filter-priority", metavar="PRIORITY", help="Filter tasks by priority")
    parser.add_argument("--complete", metavar="TASK_ID", type=int, help="Mark task as completed")
    parser.add_argument("--delete", metavar="TASK_ID", type=int, help="Delete a task")
    
    args = parser.parse_args()
    
    if args.add:
        title, description, category, priority = args.add
        task_id = task_service.add_task(title, description, category, priority, None)
        print(f"Task added with ID: {task_id}")
    
    elif args.list:
        tasks = task_service.get_all_tasks()
        for task in tasks:
            print(task)
    
    elif args.filter_category:
        tasks = task_service.get_tasks_by_category(args.filter_category)
        for task in tasks:
            print(task)
    
    elif args.filter_priority:
        tasks = task_service.get_tasks_by_priority(args.filter_priority)
        for task in tasks:
            print(task)
    
    elif args.complete:
        task_service.mark_task_completed(args.complete)
        print(f"Task {args.complete} marked as completed.")
    
    elif args.delete:
        task_service.delete_task(args.delete)
        print(f"Task {args.delete} deleted.")
    
if __name__ == "__main__":
    main()
