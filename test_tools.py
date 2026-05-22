from tools.ticket_tools import get_all_tickets, get_high_priority_tickets, get_ticket_metrics

print("All Tickets:")
print(get_all_tickets())

print("\nHigh Priority Tickets:")
print(get_high_priority_tickets())

print("\nTicket Metrics:")
print(get_ticket_metrics())