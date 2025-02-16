from services.task_service import TaskService
from datetime import datetime
from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)
def main():
    task_service = TaskService()

    while True:
        print(Fore.CYAN + "\nTask Manager CLI" + Style.RESET_ALL)
        print(Fore.GREEN + "1. Add Task")
        print("2. List All Tasks")
        print("3. Filter by Category")
        print("4. Filter by Priority")
        print("5. Mark Task as Completed")
        print("6. Delete Task")
        print("7. Exit")

        choice = input(Fore.YELLOW + "Choose an option: " + Style.RESET_ALL)

        try:
            if choice == "1":
                title = input("Enter task title: ").strip()
                description = input("Enter task description: ").strip()
                category = input("Enter task category: ").strip()
                priority = input("Enter task priority (Low/Medium/High): ").strip()
                due_date_str = input("Enter due date (MM/DD/YYYY) or leave blank: ")
                
                due_date = None                
                if due_date_str:
                    try:
                        due_date = datetime.strptime(due_date_str, "%m/%d/%Y").date()
                    except ValueError:
                        print(Fore.RED + "Invalid date format. Please enter in MM/DD/YYYY format.")
                        continue 
                task_id = task_service.add_task(title, description, category, priority, due_date)
                print(Fore.GREEN + f"Task added with ID: {task_id}")

            elif choice == "2":
                tasks = task_service.get_all_tasks()
                if tasks:
                    # Convert dictionary values into lists for tabulate
                    table_data = [list(task.values()) for task in tasks]
                    print(tabulate(table_data, headers=["ID", "Title", "Description", "Category", "Priority", "Due Date", "Completed"], tablefmt="grid"))
                else:
                    print(Fore.RED + "No tasks found.")

            elif choice == "3":
                category = input("Enter category: ").strip()
                tasks = task_service.get_tasks_by_category(category)
                if tasks:
                    table_data = [list(task.values()) for task in tasks]
                    print(tabulate(table_data, headers=["ID", "Title", "Description", "Category", "Priority", "Due Date", "Completed"], tablefmt="grid"))
                else:
                    print(Fore.RED + "No tasks found in this category.")

            elif choice == "4":
                try:
                    priority = input("Enter priority (Low/Medium/High): ").strip().lower()
                    tasks = task_service.get_tasks_by_priority(priority)
                    if tasks:
                        table_data = [list(task.values()) for task in tasks]  # Convert dict values to list
                        print(tabulate(table_data, headers=["ID", "Title", "Description", "Category", "Priority", "Due Date", "Completed"], tablefmt="grid"))
                    else:
                        print(Fore.RED + "No tasks found with this priority.")
                except Exception as e:
                    print(f"Unexpected error: {e}")  

            elif choice == "5":
                task_id = int(input("Enter task ID to mark as completed: "))
                task_service.mark_task_completed(task_id)
                print(Fore.GREEN + f"Task {task_id} marked as completed.")

            elif choice == "6":
                task_id = int(input("Enter task ID to delete: "))
                task_service.delete_task(task_id)
                print(Fore.RED + f"Task {task_id} deleted.")

            elif choice == "7":
                print(Fore.CYAN + "Exiting Task Manager. Goodbye!")
                break

            else:
                print(Fore.RED + "Invalid choice. Please select a valid option.")

        except ValueError:
            print(Fore.RED + "Error: Please enter a valid input.")
        except Exception as e:
            print(Fore.RED + f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
