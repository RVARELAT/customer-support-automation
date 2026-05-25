# OpsPilot AI
### AI-Powered Support Operations Platform

OpsPilot AI is an AI-driven operations platform that combines backend automation workflows with an agentic AI layer capable of analyzing support operations, monitoring ticket activity, identifying urgent issues, and generating operational summaries using backend tools and APIs.

This project simulates how modern enterprise AI systems interact with operational software rather than functioning as simple chatbots.

---

# Key Features

## AI Operations Agent
The platform includes a mock AI operations agent capable of:

- analyzing support ticket data
- identifying urgent operational issues
- generating operational summaries
- monitoring ticket metrics
- recommending actions
- detecting repeated support problems

The AI agent uses backend tools and APIs to retrieve and analyze operational data.

---

## Support Ticket Automation

Automatically processes support tickets by:

- classifying issue categories
- assigning priority levels
- recommending support actions
- flagging tickets for review

Supported ticket categories:

- billing
- refund
- outage
- hardware
- setup
- general

---

## FastAPI Backend

Built using FastAPI.

API endpoints include:

| Endpoint | Purpose |
|---|---|
| `POST /process-ticket` | Process and store support tickets |
| `GET /tickets` | Retrieve saved tickets |
| `GET /agent/summary` | Run the AI operations agent |
| `GET /health` | Backend health monitoring |

The backend acts as the operational system the AI agent interacts with.

---

## AI Tool Architecture

The AI agent does not directly access the database.

Instead, it uses tools:

```text
AI Agent
    ↓
Tool Functions
    ↓
FastAPI APIs
    ↓
SQLite Database
```

This mirrors modern enterprise AI system design where agents interact with operational software through controlled tool interfaces.

---

# Interactive Dashboard

Built using Streamlit.

Dashboard capabilities:

- submit support tickets
- monitor operational metrics
- search/filter tickets
- run the AI operations agent
- display AI-generated operational summaries
- view urgent ticket activity

---

# Failure Logging & Monitoring

Automation failures are logged automatically into:

```text
automation_failures.log
```

This simulates real-world operational monitoring and reliability workflows.

---

# Tech Stack

## Backend & APIs
- Python
- FastAPI
- SQLAlchemy
- SQLite

## AI / Agent Layer
- Python
- Tool-based agent architecture
- Operational reasoning workflows

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
FastAPI Backend APIs
        ↓
AI Operations Agent
        ↓
Tool Functions
        ↓
Operational Ticket System
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
├── agent/
│   └── agent.py
├── tools/
│   └── ticket_tools.py
├── requirements.txt
├── support_tickets.db
├── automation_failures.log
└── README.md
```

---

# Example AI Workflow

## User Action

```text
Generate Operations Summary
```

## AI Agent Workflow

```text
1. Call backend ticket tools
2. Retrieve support ticket data
3. Analyze ticket metrics
4. Detect urgent operational issues
5. Generate operational summary
6. Recommend actions
```

---

# Example AI Operations Report

```text
Operations Summary:
There are 15 total support tickets. 4 are high priority and 3 require manual review.

Biggest Issue:
The most common ticket category is 'outage'.

Main Concern:
There are multiple urgent tickets requiring immediate attention.

Recommended Actions:
Review high priority tickets first and investigate repeated outage-related issues.
```

---

# Engineering Concepts Practiced

This project demonstrates:

- backend API development
- database integration
- CRUD operations
- automation workflows
- AI agent orchestration
- tool-based AI systems
- operational monitoring
- failure logging
- dashboard development
- Git/GitHub workflow
- virtual environments
- dependency management
- system architecture design

---

# Why This Project Matters

This project focuses on operational AI systems rather than generic chatbots.

The AI agent interacts with backend systems, APIs, and operational data to simulate real-world enterprise AI workflows used in:

- internal tooling
- customer operations
- platform engineering
- operational automation
- AI operations systems

---

# Future Improvements

Potential future upgrades:

- real OpenAI API integration
- automated incident reports
- Slack/email alerts
- multi-agent workflows
- PostgreSQL migration
- Docker deployment
- ticket trend analysis
- scheduled monitoring agents
- AI-generated customer responses

---

# Author

Ricardo Varela Tellez

UCLA — Computer Science & Linguistics
