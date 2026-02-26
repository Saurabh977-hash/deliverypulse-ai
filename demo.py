import streamlit as st
from agent import generate_delivery_report, SAMPLE_JIRA, SAMPLE_VELOCITY

st.set_page_config(page_title="DeliveryPulse AI", layout="wide")
st.title("🚀 DeliveryPulse AI")
st.markdown("**Agentic AI Copilot for Delivery Dashboards** – Instant executive reports from Jira data.")

jira_input = st.text_area("Paste Jira CSV (or use sample):", SAMPLE_JIRA, height=150)
velocity_input = st.text_input("Velocity trend:", SAMPLE_VELOCITY)

if st.button("Generate Report", type="primary"):
    with st.spinner("Analyzing delivery health..."):
        report = generate_delivery_report(jira_input, velocity_input)
        st.markdown("### 📊 Delivery Status Report")
        st.markdown(report)
        st.success("DeliveryPulse AI (live demo) - Report generated in seconds!")

