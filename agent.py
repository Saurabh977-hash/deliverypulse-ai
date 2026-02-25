import os
from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("CLAUDE_API_KEY", "demo-mode"))

SAMPLE_JIRA = """
Ticket,Status,Sprint,Story Points,Blocker
PROJ-101,In Progress,Sprint 23,8,None
PROJ-102,Done,Sprint 23,5,None
PROJ-103,In Progress,Sprint 23,13,Database lag
PROJ-104,Blocked,Sprint 23,3,Auth API down
PROJ-105,To Do,Sprint 24,5,None
"""

SAMPLE_VELOCITY = "Sprint 20: 34pts, Sprint 21: 42pts, Sprint 22: 28pts, Sprint 23: 35pts (target)"

def generate_delivery_report(jira_input, velocity_input):
    prompt = f"""
    You are DeliveryPulse, an AI delivery copilot...
    (your existing prompt text, using jira_input and velocity_input)
    """

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1500,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt}
                ],
            }
        ],
    )

    return response.content[0].text

