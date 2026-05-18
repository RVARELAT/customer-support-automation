# Import create_engine
# This creates the database connection
from sqlalchemy import create_engine

# Import sessionmaker
# This helps us interact with the database
from sqlalchemy.orm import sessionmaker

# Import declarative_base
# Used to create database models/classes
from sqlalchemy.orm import declarative_base


# Database URL
# sqlite:/// means:
# use SQLite database
#
# support_tickets.db will be the database file name
DATABASE_URL = "sqlite:///./support_tickets.db"


# Create the database engine
# Think of this as the connection to the database
engine = create_engine(DATABASE_URL)


# Create database session factory
# Sessions allow Python to talk to the database
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for database models
# Other models/tables will inherit from this
Base = declarative_base()