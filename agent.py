from anthropic import Anthropic

client = Anthropic(api_key="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")

SAMPLE_JIRA = """
Ticket,Status,Sprint,Story Points,Blocker
PROJ-101,In Progress,Sprint 23,8,None
PROJ-102,Done,Sprint 23,5,None
PROJ-103,In Progress,Sprint 23,13,Database lag
PROJ-104,Blocked,Sprint 23,3,Auth API down
PROJ-105,To Do,Sprint 24,5,None
"""

SAMPLE_VELOCITY = "Sprint 20: 34pts, Sprint 21: 42pts, Sprint 22: 28pts, Sprint 23: 35pts (target)"

def generate_delivery_report(jira_data, velocity_data):
    prompt = f"""
    You are DeliveryPulse AI, an agentic copilot for program executives. 
    Generate a professional delivery status report from this Jira data: {jira_data}
    Velocity trend: {velocity_data}
    
    Include:
    - Executive summary (1 para)
    - Risk matrix (table)
    - Action items
    - Velocity chart summary
    Format as Markdown email-ready.
    """
    
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text
