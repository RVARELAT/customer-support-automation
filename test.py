from backend.automation import process_ticket

ticket = "My internet has been down for 3 days and I want a refund."

result = process_ticket(ticket)

print(result)