import os
from datetime import datetime
from task_manager.tasks import load_tasks, add_task, save_tasks, sort_tasks_by_priority_and_due_date, mark_task_complete

# Clears screen to prevent clogging terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter_to_continue():
    input("\nPress Enter to continue...")

def display_menu():
    # Display the main menu options.
    print("\n==============================")
    print("   Task Manager Menu")
    print("==============================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Explain Priority Levels")
    print("5. Exit")

def display_tasks(tasks):
    # Display tasks sorted by priority and due date that are not completed.
    print("\n===== Task List =====")
    sorted_tasks = sort_tasks_by_priority_and_due_date(tasks)
    for i, (task, status, due_date, priority, recurring, description) in enumerate(sorted_tasks, 1):
        if status != "Completed":
            print(f"{i}. {task} | Status: {status} | Due: {due_date} | Priority: {priority} | Recurrence: {recurring}")
            if description:
                print(f"   Description: {description}")
    print("\n=====================")

def explain_priority():
    print("\nPriority Levels Explanation:")
    print("1. Utmost Importance - These tasks are critical and should be done as soon as possible.")
    print("2. Do When Possible - These tasks are important, but can wait until you have some free time.")
    print("3. Can Wait - These tasks are not urgent and can be done when there is no higher priority task.")
    print("\n=====================")

# Validates date input in MM/DD/YY format
def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%m/%d/%y")
    except ValueError:
        print("Invalid date format. Please use MM/DD/YY.")
        return None

# Validates time input in HH:MM format
def validate_time(time_str):
    try:
        return datetime.strptime(time_str, "%H:%M").time()
    except ValueError:
        print("Invalid time format. Please use HH:MM (24-hour format).")
        return None

def mark_task_complete(tasks, task_num):
    # Mark a task as completed.
    task = tasks[task_num]
    task[1] = "Completed"
    save_tasks(tasks)
    print(f"\nTask '{task[0]}' marked as completed.")

# Main
def main():
    tasks = load_tasks()

    while True:
        clear_screen()  # Clear the screen before each action
        display_menu()

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            task = input("Enter task: ")
            due_date_str = input("Enter due date (MM/DD/YY): ")

            # Validate the date input
            due_date = validate_date(due_date_str)
            if due_date is None:
                press_enter_to_continue()
                continue  # Skip adding task if date is invalid

            # Ask for time input (optional)
            include_time = input("Do you want to include a time for the due date? (yes/no): ").lower()
            if include_time in ['y', 'yes']:
                due_time_str = input("Enter due time (HH:MM): ")
                due_time = validate_time(due_time_str)
                if due_time is None:
                    press_enter_to_continue()
                    continue  # Skip adding task if time is invalid
                due_date = datetime.combine(due_date, due_time)
            elif include_time in ['n', 'no']:
                due_date = due_date.date()  # Keep only the date part if no time is given
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                press_enter_to_continue()
                continue  # Skip adding task if input is invalid

            # Priority input with numeric choices
            priority_input = input("Enter priority (1 for Utmost Importance, 2 for Do When Possible, 3 for Can Wait): ")
            priority_map = {
                "1": "Utmost Importance",
                "2": "Do When Possible",
                "3": "Can Wait"
            }
            priority = priority_map.get(priority_input, "Can Wait")  # Default to "Can Wait" if invalid input

            recurring = input("Enter recurrence (None, Daily, Weekly, Monthly): ")

            # Input for task description (max 150 characters)
            description = input("Enter task description (max 150 characters): ")
            if len(description) > 150:
                print("Description is too long. Please keep it under 150 characters.")
                press_enter_to_continue()
                continue

            # Add the task
            add_task(tasks, task, due_date, priority, recurring, description)
            press_enter_to_continue()

        elif choice == "2":
            display_tasks(tasks)
            press_enter_to_continue()

        elif choice == "3":
            display_tasks(tasks)  # Display tasks first
            task_num = input("\nEnter the number of the task to mark as complete: ")

            try:
                task_num = int(task_num) - 1  # Convert to 0-based index
                if task_num < 0 or task_num >= len(tasks):
                    print("Invalid task number.")
                    press_enter_to_continue()
                    continue

                # Mark the task as complete
                mark_task_complete(tasks, task_num)

                press_enter_to_continue()

            except ValueError:
                print("Invalid input. Please enter a number.")
                press_enter_to_continue()

        elif choice == "4":
            explain_priority()  # Show the priority explanation
            press_enter_to_continue()

        elif choice == "5":
            print("Goodbye!")
            save_tasks(tasks)  # Save the tasks before exiting
            break

        else:
            print("Invalid option. Please try again.")
            press_enter_to_continue()

if __name__ == "__main__":
    main()
