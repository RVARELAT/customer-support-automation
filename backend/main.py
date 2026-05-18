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

    # Process the ticket using our automation logic
    result = process_ticket(ticket.ticket_text)

    # Return the processed result
    return result