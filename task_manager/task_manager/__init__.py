from .tasks import load_tasks, add_task, save_tasks
from .logging import log_event

priority_map = {
    1: "Utmost Importance",
    2: "Do When Possible",
    3: "Can Wait"
}

def sort_tasks_by_priority_and_due_date(tasks):
    # Sort tasks by priority (highest priority first) and due date (earliest date first).
    # Assumes tasks are tuples (task_name, status, due_date, priority, recurrence).
    
    sorted_tasks = sorted(tasks, key=lambda task: (task[3], task[2]))  # task[3] is priority, task[2] is due_date
    return sorted_tasks
