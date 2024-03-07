import sqlite3
from datetime import datetime

# Database file to store tasks
DB_FILE = 'tasks.db'


def create_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        priority TEXT,
                        due_date TEXT,
                        completed INTEGER)''')
    conn.commit()
    conn.close()


def add_task_to_db(title, priority, due_date):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, priority, due_date, completed) VALUES (?, ?, ?, ?)",
                   (title, priority, due_date, 0))
    conn.commit()
    conn.close()


def remove_task_from_db(task_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()


def mark_task_completed_in_db(task_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed=1 WHERE id=?", (task_id,))
    conn.commit()
    conn.close()


def get_all_tasks():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks


def display_tasks(tasks):
    print("Tasks:")
    for task in tasks:
        status = "Completed" if task[4] else "Pending"
        print(f"{task[0]}. {task[1]} - Priority: {task[2]} - Due Date: {task[3]} - Status: {status}")


def display_tasks_by_priority(priority):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
    tasks = cursor.fetchall()
    conn.close()

    print(f"Tasks with priority '{priority}':")
    for task in tasks:
        status = "Completed" if task[4] else "Pending"
        print(f"{task[0]}. {task[1]} - Priority: {task[2]} - Due Date: {task[3]} - Status: {status}")


def main():
    create_database()

    while True:
        print("\nMenu:\n")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display all Tasks")
        print("5. Display Tasks by Priority")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            priority = input("Enter task priority (high/medium/low): ")
            due_date_str = input("Enter due date (YYYY-MM-DD), press Enter if not applicable: ")
            due_date = due_date_str if due_date_str else None
            add_task_to_db(title, priority, due_date)
        elif choice == '2':
            tasks = get_all_tasks()
            display_tasks(tasks)
            task_id = int(input("Enter task ID to remove: "))
            remove_task_from_db(task_id)
        elif choice == '3':
            tasks = get_all_tasks()
            display_tasks(tasks)
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_task_completed_in_db(task_id)
        elif choice == '4':
            tasks = get_all_tasks()
            display_tasks(tasks)
        elif choice == '5':
            priority = input("Enter priority to display (high/medium/low): ")
            display_tasks_by_priority(priority)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
