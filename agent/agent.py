# Import ticket tools
# These are the functions the agent can use
from tools.ticket_tools import (
    get_all_tickets,
    get_high_priority_tickets,
    get_ticket_metrics
)


# Simple AI operations agent
# For now, this is rule-based.
# Later, we can connect it to the OpenAI API.
def run_operations_agent():

    # Get all ticket data
    tickets = get_all_tickets()

    # Get high priority tickets
    high_priority_tickets = get_high_priority_tickets()

    # Get ticket metrics
    metrics = get_ticket_metrics()

    # Create a summary dictionary
    summary = {
        "summary": "Operations report generated successfully.",
        "metrics": metrics,
        "high_priority_tickets": high_priority_tickets,
        "recommendation": "Review high priority tickets first and monitor repeated issue categories."
    }

    return summary