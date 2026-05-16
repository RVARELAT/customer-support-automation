def classify_ticket(ticket_text: str) -> str:
    text = ticket_text.lower()

    if any(word in text for word in ["refund", "money back", "chargeback"]):
        return "refund"

    if any(word in text for word in ["down", "outage", "not working", "no internet"]):
        return "outage"

    if any(word in text for word in ["router", "device", "hardware", "modem"]):
        return "hardware"

    if any(word in text for word in ["setup", "install", "activate"]):
        return "setup"

    if any(word in text for word in ["bill", "invoice", "charged", "payment"]):
        return "billing"

    return "general"


def assign_priority(ticket_text: str, category: str) -> str:
    text = ticket_text.lower()

    urgent_words = [
        "urgent",
        "angry",
        "cancel",
        "broken",
        "terrible",
        "3 days",
        "not working"
    ]

    if category == "outage":
        return "high"

    if any(word in text for word in urgent_words):
        return "high"

    if category in ["refund", "billing", "hardware"]:
        return "medium"

    return "low"


def suggest_action(category: str, priority: str) -> str:
    actions = {
        "refund": "Check refund eligibility and order history.",
        "outage": "Escalate to technical support.",
        "hardware": "Schedule troubleshooting or replacement.",
        "setup": "Send setup instructions.",
        "billing": "Review payment and invoice history.",
        "general": "Route to support team."
    }

    action = actions.get(category, "Route to support team.")

    if priority == "high":
        action += " Mark for urgent review."

    return action


def process_ticket(ticket_text: str) -> dict:
    category = classify_ticket(ticket_text)

    priority = assign_priority(ticket_text, category)

    action = suggest_action(category, priority)

    return {
        "ticket_text": ticket_text,
        "category": category,
        "priority": priority,
        "suggested_action": action,
        "status": "needs_review" if priority == "high" else "automated"
    }