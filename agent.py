import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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
    You are DeliveryPulse, an AI delivery copilot for IT delivery leaders.

    Input Jira snapshot:
    {jira_input or SAMPLE_JIRA}

    Input velocity/risk snapshot:
    {velocity_input or SAMPLE_VELOCITY}

    Analyse trends, blockers, risks, and give a crisp executive summary,
    plus 3–5 concrete actions.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",   # or a similar Gemini model name
        contents=prompt,
        max_output_tokens=1500,
    )

    return response.text



