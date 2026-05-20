# Import Streamlit
# Streamlit helps us build simple dashboards with Python
import streamlit as st

# Import requests
# requests lets this dashboard call our FastAPI backend
import requests

# Import pandas
# pandas helps us work with table/data metrics
import pandas as pd


# Backend API URL
# This is where our FastAPI server is running
API_URL = "http://127.0.0.1:8000"


# Dashboard title
st.title("Customer Support Automation Dashboard")


# Small description under the title
st.write("Monitor processed support tickets and automation results.")


# Call the FastAPI /tickets endpoint
# This asks the backend for all saved tickets
response = requests.get(f"{API_URL}/tickets")


# Check if the API request worked
if response.status_code == 200:

    # Convert the JSON response into Python data
    tickets = response.json()

    # If there are saved tickets, show metrics
    if tickets:

        # Convert tickets into a pandas DataFrame
        df = pd.DataFrame(tickets)

        # Calculate metrics
        total_tickets = len(df)
        high_priority = len(df[df["priority"] == "high"])
        automated = len(df[df["status"] == "automated"])
        needs_review = len(df[df["status"] == "needs_review"])

        # Create 4 metric boxes
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Tickets", total_tickets)
        col2.metric("High Priority", high_priority)
        col3.metric("Automated", automated)
        col4.metric("Needs Review", needs_review)

        # Show all tickets in a table
        st.subheader("Saved Tickets")
        st.dataframe(df)

    else:
        st.info("No tickets found yet. Process a ticket first.")

else:
    st.error("Could not connect to the FastAPI backend.")