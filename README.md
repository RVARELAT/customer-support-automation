# Customer Support Automation System

An internal operations tool that automates customer support ticket processing using Python, FastAPI, SQLite, and Streamlit.

This project simulates a real-world customer support automation workflow by:
- classifying support tickets
- assigning priority levels
- recommending actions
- storing ticket data
- monitoring automation results
- logging failures
- displaying operational metrics in a dashboard

---

# Features

## Ticket Automation
- Detects support ticket categories
- Assigns urgency levels
- Suggests support actions automatically

Supported categories:
- billing
- refund
- outage
- hardware
- setup
- general

---

## Backend API
Built using FastAPI.

Endpoints:
- `POST /process-ticket`
- `GET /tickets`

The backend:
- processes tickets
- stores ticket data
- retrieves saved tickets
- handles automation failures

---

## Database Integration
Uses SQLite + SQLAlchemy for persistent storage.

Stored ticket data includes:
- ticket text
- category
- priority
- suggested action
- automation status

---

## Interactive Dashboard
Built with Streamlit.

Dashboard features:
- submit support tickets
- view saved tickets
- filter tickets
- monitor automation metrics

---

## Failure Logging
Automation failures are logged into:

```text
automation_failures.log
```

This simulates real-world monitoring and reliability workflows.

---

# Tech Stack

## Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite

## Frontend / Dashboard
- Streamlit

## Data & Utilities
- Pandas
- Requests

## Version Control
- Git
- GitHub

---

# System Architecture

```text
Streamlit Dashboard
        ↓
FastAPI Backend API
        ↓
Automation Workflow
        ↓
SQLite Database
        ↓
Failure Logging
```

---

# Project Structure

```text
customer-support-automation/
├── backend/
│   ├── main.py
│   ├── automation.py
│   ├── database.py
│   ├── models.py
│   └── logger.py
├── dashboard/
│   └── app.py
├── requirements.txt
├── support_tickets.db
└── README.md
```

---

# How To Run The Project

## 1. Clone Repository

```bash
git clone <YOUR_GITHUB_REPO_URL>
cd customer-support-automation
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Mac/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger API Docs:

```text
http://127.0.0.1:8000/docs
```

---

## 5. Run Streamlit Dashboard

Open another terminal:

```bash
streamlit run dashboard/app.py
```

---

# Example Workflow

1. User submits support ticket
2. Backend processes ticket
3. Automation assigns category + priority
4. Ticket saved into SQLite database
5. Dashboard displays updated metrics
6. Failures are logged automatically

---

# Example Ticket

Input:

```text
"My internet has been down for 3 days and I want a refund."
```

Output:

```json
{
  "category": "refund",
  "priority": "high",
  "suggested_action": "Check refund eligibility and order history. Mark for urgent review.",
  "status": "needs_review"
}
```

---

# Engineering Concepts Practiced

- backend API development
- database integration
- CRUD operations
- automation workflows
- failure handling
- logging and monitoring
- dashboard development
- Git/GitHub workflow
- virtual environments
- dependency management

---

# Future Improvements

Possible future features:
- AI-powered ticket classification
- OpenAI-generated responses
- authentication/login system
- PostgreSQL migration
- Docker deployment
- Slack/email alerts
- analytics dashboard

---

# Author

Ricardo Varela Tellez

UCLA — Computer Science & Linguistics