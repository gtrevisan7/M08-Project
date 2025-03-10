import logging

# Configure the logging system
logging.basicConfig(
    filename="task_manager.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def log_event(message):
    # Log an event.
    logging.info(message)
