import os
from datetime import datetime
from task_manager.logging import log_event

TASK_FILE = "tasks.txt"

# Priority Levels
PRIORITY_LEVELS = {
    1: "Utmost Importance",  # Most important
    2: "Do When Possible",   # Medium importance
    3: "Can Wait"            # Least important
}

def add_task(tasks, task_name, due_date, priority, recurring, description):
    # Add a new task with priority and description.
    priority_level = get_priority_level(priority)
    tasks.append([task_name, "Pending", due_date, priority_level, recurring, description])  # Save priority as a number
    save_tasks(tasks)
    log_event(f"Task added: {task_name}, Due: {due_date}, Priority: {priority_level}, Recurrence: {recurring}, Description: {description}")
    print("Task added!")

def get_priority_level(priority):
    # Convert priority input into level (number).
    priority = priority.lower()
    if priority == "utmost importance":
        return 1
    elif priority == "do when possible":
        return 2
    elif priority == "can wait":
        return 3
    else:
        print("Invalid priority, defaulting to 'can wait'.")
        return 3

def save_tasks(tasks):
    # Save tasks to the file.
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            # Save the task details, including status
            file.write(f"{task[0]},{task[1]},{task[2].strftime('%m/%d/%y')},{task[3]},{task[4]},{task[5]}\n")

def load_tasks():
    # Load tasks from the file.
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                fields = line.strip().split(",")
                
                # Ensure there are exactly 6 fields (task, status, due_date, priority, recurring, description)
                if len(fields) == 6:
                    task, status, due_date_str, priority, recurring, description = fields

                    try:
                        due_date = datetime.strptime(due_date_str, "%m/%d/%y")
                    except ValueError:
                        due_date = None  # Handle invalid date formats
                    
                    # Convert priority to an integer (it should be a number, not a string)
                    try:
                        priority = int(priority)
                    except ValueError:
                        priority = 3  # Default to "Can Wait" if there's an invalid priority
                    
                    tasks.append([task, status, due_date, priority, recurring, description])
                else:
                    print(f"Skipping invalid task line: {line.strip()}")
    return tasks

def mark_task_complete(tasks, task_index):
    # Mark a task as completed.
    if 0 <= task_index < len(tasks):
        task = tasks[task_index]
        task[1] = "Completed"
        save_tasks(tasks)
        print(f"\nTask '{task[0]}' marked as completed!")
    else:
        print("Invalid task index.")

def sort_tasks_by_priority_and_due_date(tasks):
    return sorted(tasks, key=lambda x: (x[3], x[2]))
