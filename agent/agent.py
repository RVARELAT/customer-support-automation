# Import ticket tools
# These tools let the agent read ticket data from the backend
from tools.ticket_tools import (
    get_all_tickets,
    get_high_priority_tickets,
    get_ticket_metrics
)


# Generate a mock AI operations report
# This simulates AI-style reasoning without using the OpenAI API
def generate_mock_ai_report(metrics, tickets, high_priority_tickets):

    # Start report sections
    report_sections = []

    # Add main summary
    report_sections.append(
        f"Operations Summary: There are {metrics['total_tickets']} total support tickets. "
        f"{metrics['high_priority_tickets']} are high priority, "
        f"{metrics['automated_tickets']} were automated, and "
        f"{metrics['needs_review_tickets']} need manual review."
    )

    # Find the most common ticket category
    category_counts = {}

    for ticket in tickets:
        category = ticket["category"]

        if category not in category_counts:
            category_counts[category] = 0

        category_counts[category] += 1

    # If there are tickets, find biggest category
    if category_counts:
        biggest_category = max(category_counts, key=category_counts.get)
        biggest_category_count = category_counts[biggest_category]

        report_sections.append(
            f"Biggest Issue: The most common ticket category is '{biggest_category}' "
            f"with {biggest_category_count} ticket(s)."
        )

    # Add concern based on high priority tickets
    if metrics["high_priority_tickets"] > 0:
        report_sections.append(
            "Main Concern: There are high priority tickets that may need immediate attention."
        )
    else:
        report_sections.append(
            "Main Concern: There are currently no high priority tickets."
        )

    # Add review concern
    if metrics["needs_review_tickets"] > 0:
        report_sections.append(
            "Manual Review: Some tickets need human review before being resolved."
        )

    # Add recommended actions
    recommendations = []

    if metrics["high_priority_tickets"] > 0:
        recommendations.append("Review high priority tickets first.")

    if metrics["needs_review_tickets"] > 0:
        recommendations.append("Check tickets marked as needs_review.")

    if category_counts:
        recommendations.append(f"Monitor repeated '{biggest_category}' issues.")

    if not recommendations:
        recommendations.append("Continue monitoring ticket activity.")

    report_sections.append(
        "Recommended Actions: " + " ".join(recommendations)
    )

    # Add urgent ticket summary
    if high_priority_tickets:
        report_sections.append(
            f"Urgent Tickets: {len(high_priority_tickets)} ticket(s) should be reviewed immediately."
        )

    # Join all sections into one report
    return "\n\n".join(report_sections)


# Main operations agent function
# This is the function our backend/dashboard will run
def run_operations_agent():

    # Get all tickets from backend
    tickets = get_all_tickets()

    # Get high priority tickets from backend
    high_priority_tickets = get_high_priority_tickets()

    # Get ticket metrics from backend
    metrics = get_ticket_metrics()

    # Generate mock AI report
    ai_report = generate_mock_ai_report(
        metrics,
        tickets,
        high_priority_tickets
    )

    # Return agent result
    return {
        "summary": "Mock AI operations report generated successfully.",
        "metrics": metrics,
        "high_priority_tickets": high_priority_tickets,
        "ai_report": ai_report
    }