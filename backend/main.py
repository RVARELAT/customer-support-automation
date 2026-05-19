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


# Create a POST endpoint
# POST means we are sending data to the server
@app.post("/process-ticket")

# This function runs when someone sends a ticket
def process_support_ticket(ticket: TicketRequest):

    # Run automation workflow
    result = process_ticket(ticket.ticket_text)

    # Create database session
    # This allows us to communicate with the database
    db = SessionLocal()

    # Create Ticket object for database
    new_ticket = Ticket(

        # Save original ticket text
        ticket_text=result["ticket_text"],

        # Save detected category
        category=result["category"],

        # Save assigned priority
        priority=result["priority"],

        # Save suggested action
        suggested_action=result["suggested_action"],

        # Save ticket status
        status=result["status"]
    )

    # Add ticket to database session
    db.add(new_ticket)

    # Commit/save changes permanently
    db.commit()

    # Close database session
    db.close()

    # Return processed ticket result
    return result


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