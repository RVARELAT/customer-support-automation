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


# Ticket submission section
st.subheader("Submit New Support Ticket")

# Text area where user can type a support ticket
ticket_text = st.text_area(
    "Enter customer support ticket:",
    placeholder="Example: My internet has been down for 3 days and I want a refund."
)

# Button to submit the ticket
if st.button("Process Ticket"):

    # Make sure the user typed something
    if ticket_text.strip():

        # Send the ticket to the FastAPI backend
        response = requests.post(
            f"{API_URL}/process-ticket",
            json={"ticket_text": ticket_text}
        )

        # If the request worked, show success message
        if response.status_code == 200:
            result = response.json()

            st.success("Ticket processed successfully!")

            st.write("Category:", result["category"])
            st.write("Priority:", result["priority"])
            st.write("Suggested Action:", result["suggested_action"])
            st.write("Status:", result["status"])

        # If something went wrong, show error
        else:
            st.error("Something went wrong while processing the ticket.")

    # If text box is empty, warn the user
    else:
        st.warning("Please enter a ticket before submitting.")


# Divider line
st.divider()


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

        # # Show all tickets in a table
        # st.subheader("Saved Tickets")
        # st.dataframe(df)
        
        # Show filters for saved tickets
        st.subheader("Filter Tickets")

        # Create 3 filter dropdowns
        category_filter = st.selectbox(
            "Filter by category",
            ["All"] + sorted(df["category"].unique().tolist())
        )

        priority_filter = st.selectbox(
            "Filter by priority",
            ["All"] + sorted(df["priority"].unique().tolist())
        )

        status_filter = st.selectbox(
            "Filter by status",
            ["All"] + sorted(df["status"].unique().tolist())
        )
        
        # Search box for tickets
        search_text = st.text_input(
            "Search tickets",
            placeholder="Search by refund, outage, billing, high, automated..."
        )

        # Start with all tickets
        filtered_df = df.copy()
        
        # Apply search filter if user typed something
        if search_text.strip():
            search_lower = search_text.lower()

            filtered_df = filtered_df[
                filtered_df["ticket_text"].str.lower().str.contains(search_lower)
                | filtered_df["category"].str.lower().str.contains(search_lower)
                | filtered_df["priority"].str.lower().str.contains(search_lower)
                | filtered_df["status"].str.lower().str.contains(search_lower)
                | filtered_df["suggested_action"].str.lower().str.contains(search_lower)
            ]

        # Apply category filter if user selected a category
        if category_filter != "All":
            filtered_df = filtered_df[filtered_df["category"] == category_filter]

        # Apply priority filter if user selected a priority
        if priority_filter != "All":
            filtered_df = filtered_df[filtered_df["priority"] == priority_filter]

        # Apply status filter if user selected a status
        if status_filter != "All":
            filtered_df = filtered_df[filtered_df["status"] == status_filter]
        
        
        # Show filtered tickets
        st.subheader("Saved Tickets")
        st.dataframe(filtered_df)
        

    else:
        st.info("No tickets found yet. Process a ticket first.")

else:
    st.error("Could not connect to the FastAPI backend.")