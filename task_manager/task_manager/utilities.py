from datetime import datetime

def format_due_date(due_date_str):
    # Helper function to format the due date string to datetime.
    return datetime.strptime(due_date_str, "%Y-%m-%d").date()
