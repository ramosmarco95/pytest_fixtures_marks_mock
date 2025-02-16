# handles task CRUD operations

import sqlite3

class TaskModel:
    
    def __init__(self, db_name = "tasks.db"):
        self.db_name = db_name
        self._create_table()
        
    def _create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    category TEXT,
                    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
                    due_date TEXT,
                    status TEXT CHECK(status IN ('Pending', 'Completed')) DEFAULT 'Pending'
                )
            ''')
            conn.commit()
            
    def get_all_tasks(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row  # Converts rows into dictionary-like objects
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks")
            tasks = cursor.fetchall()
            return [dict(task) for task in tasks]  # Convert rows to list of dictionaries
            
    def add_task(self, title, description, category, priority, due_date=None):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO tasks (title, description, category, priority, due_date, status)
                VALUES (?, ?, ?, ?, ?, 'Pending')
            ''', (title, description, category, priority, due_date))

            conn.commit()
            return cursor.lastrowid  # Return new task ID
        
    def update_task_status(self, task_id, status):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
            conn.commit()
            return cursor.rowcount
        
    def delete_task(self, task_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()
            return cursor.rowcount
        
    