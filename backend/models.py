# Import database column types
from sqlalchemy import Column, Integer, String

# Import Base from database.py
from backend.database import Base

# Create Ticket table/model
# This represents support tickets in the database
class Ticket(Base):

    # Name of the database table
    __tablename__ = "tickets"

    # Ticket ID
    # Primary key means unique identifier
    id = Column(Integer, primary_key=True, index=True)

    # Original support ticket text
    ticket_text = Column(String)

    # Detected category
    category = Column(String)

    # Assigned priority
    priority = Column(String)

    # Suggested action
    suggested_action = Column(String)

    # Ticket status
    status = Column(String)