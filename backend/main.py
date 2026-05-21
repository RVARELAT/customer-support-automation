# Import FastAPI framework
# FastAPI helps us build backend APIs quickly
from fastapi import FastAPI

# Import BaseModel from Pydantic
# Pydantic helps validate incoming data
from pydantic import BaseModel

# Import our ticket automation function
# This lets main.py use the logic we built in automation.py
from backend.automation import process_ticket


from backend.database import engine
from backend.models import Ticket
from backend.database import Base

from backend.database import SessionLocal

from backend.logger import log_failure



# Create the FastAPI application
# Think of this as creating the backend server
app = FastAPI()

# Create database tables automatically
Base.metadata.create_all(bind=engine)

# Create a data model for incoming support tickets
# This defines what data the API expects
class TicketRequest(BaseModel):

    # ticket_text must be a string
    # Example:
    # {
    #   "ticket_text": "My internet is down"
    # }
    ticket_text: str


# Create a GET endpoint for the homepage
# GET means we are retrieving information
@app.get("/")

# Define the function for this endpoint
def home():

    # Return a simple JSON response
    return {
        "message": "Customer Support Automation API is running"
    }



# # Create a POST endpoint
# # POST means we are sending data to the server
# @app.post("/process-ticket")

# # This function runs when someone sends a ticket
# def process_support_ticket(ticket: TicketRequest):

#     # Run automation workflow
#     result = process_ticket(ticket.ticket_text)

#     # Create database session
#     # This allows us to communicate with the database
#     db = SessionLocal()

#     # Create Ticket object for database
#     new_ticket = Ticket(

#         # Save original ticket text
#         ticket_text=result["ticket_text"],

#         # Save detected category
#         category=result["category"],

#         # Save assigned priority
#         priority=result["priority"],

#         # Save suggested action
#         suggested_action=result["suggested_action"],

#         # Save ticket status
#         status=result["status"]
#     )

#     # Add ticket to database session
#     db.add(new_ticket)

#     # Commit/save changes permanently
#     db.commit()

#     # Close database session
#     db.close()

#     # Return processed ticket result
#     return result


# Create a POST endpoint
# POST means we are sending data to the server
@app.post("/process-ticket")
def process_support_ticket(ticket: TicketRequest):

    # Try to process and save the ticket
    try:

        # Run the automation workflow from automation.py
        result = process_ticket(ticket.ticket_text)

        # Open a database session
        db = SessionLocal()

        # Create a new Ticket row using the automation result
        new_ticket = Ticket(
            ticket_text=result["ticket_text"],
            category=result["category"],
            priority=result["priority"],
            suggested_action=result["suggested_action"],
            status=result["status"]
        )

        # Stage the new ticket to be saved
        db.add(new_ticket)

        # Permanently save it to the database
        db.commit()

        # Close the database session
        db.close()

        # Return the automation result back to the user/API
        return result

    # If anything goes wrong, this block runs
    except Exception as error:

        # Save the failure details to the log file
        log_failure(ticket.ticket_text, str(error))

        # Return an error response
        return {
            "status": "failed",
            "ticket_text": ticket.ticket_text,
            "error": str(error)
        }



# Create a GET endpoint to view all saved tickets
# GET means we are retrieving data from the server
@app.get("/tickets")
def get_all_tickets():
    # Open a database session
    db = SessionLocal()

    # Get all tickets from the Ticket table
    tickets = db.query(Ticket).all()

    # Close the database session
    db.close()

    # Return all saved tickets
    return tickets