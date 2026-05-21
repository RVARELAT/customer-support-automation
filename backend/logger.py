# Import datetime
# This lets us record when an error happened
from datetime import datetime


# Function to log automation failures
def log_failure(ticket_text: str, error_message: str):

    # Open the failure log file in append mode
    # "a" means add to the file instead of replacing it
    with open("automation_failures.log", "a") as file:

        # Write the time, ticket text, and error message
        file.write(
            f"[{datetime.now()}] "
            f"Ticket: {ticket_text} | "
            f"Error: {error_message}\n"
        )