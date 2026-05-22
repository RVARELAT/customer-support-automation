# Import requests
# This lets Python call our FastAPI backend API
import requests


# Base URL for our FastAPI backend
# This is where the customer support automation API runs locally
API_URL = "http://127.0.0.1:8000"


# Tool: get all tickets
# This function asks the backend for all saved support tickets
def get_all_tickets():

    # Send a GET request to the /tickets endpoint
    response = requests.get(f"{API_URL}/tickets")

    # If the request worked, return the ticket data
    if response.status_code == 200:
        return response.json()

    # If the request failed, return an error message
    return {
        "error": "Could not fetch tickets from backend",
        "status_code": response.status_code
    }


# Tool: get high priority tickets
# This function filters tickets and returns only urgent ones
def get_high_priority_tickets():

    # First get all tickets from the backend
    tickets = get_all_tickets()

    # If something went wrong, return the error
    if isinstance(tickets, dict) and "error" in tickets:
        return tickets

    # Keep only tickets where priority is high
    high_priority_tickets = [
        ticket for ticket in tickets
        if ticket["priority"] == "high"
    ]

    # Return high priority tickets
    return high_priority_tickets


# Tool: get ticket metrics
# This function calculates simple metrics from saved tickets
def get_ticket_metrics():

    # Get all tickets from backend
    tickets = get_all_tickets()

    # If something went wrong, return the error
    if isinstance(tickets, dict) and "error" in tickets:
        return tickets

    # Count total tickets
    total_tickets = len(tickets)

    # Count high priority tickets
    high_priority_count = len([
        ticket for ticket in tickets
        if ticket["priority"] == "high"
    ])

    # Count automated tickets
    automated_count = len([
        ticket for ticket in tickets
        if ticket["status"] == "automated"
    ])

    # Count tickets that need review
    needs_review_count = len([
        ticket for ticket in tickets
        if ticket["status"] == "needs_review"
    ])

    # Return metrics as a dictionary
    return {
        "total_tickets": total_tickets,
        "high_priority_tickets": high_priority_count,
        "automated_tickets": automated_count,
        "needs_review_tickets": needs_review_count
    }