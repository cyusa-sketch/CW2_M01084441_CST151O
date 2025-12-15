import streamlit as st
import os
import google.generativeai as genai
from app.data.incidents import get_all_incidents

st.title("AI Incident Analyzer")
st.write("Select an incident and let AI explain it.")

# API key
api_key = None
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.warning("AI feature unavailable. API key not found.")
    st.stop()

st.success("API key detected.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

incidents = get_all_incidents()

if incidents.empty:
    st.info("No incidents available.")
    st.stop()

options = [
    f"{row['id']} - {row['incident_type']} ({row['severity']})"
    for _, row in incidents.iterrows()
]

choice = st.selectbox("Choose an incident:", options)
incident_id = int(choice.split("-")[0])
incident = incidents[incidents["id"] == incident_id].iloc[0]

st.subheader("Incident Details")
st.write("Type:", incident["incident_type"])
st.write("Severity:", incident["severity"])
st.write("Status:", incident["status"])
st.write("Description:", incident["description"])

if st.button("Analyze Incident"):
    prompt = f"""
Explain this cybersecurity incident in simple student language.

Type: {incident['incident_type']}
Severity: {incident['severity']}
Description: {incident['description']}
"""

    try:
        with st.spinner("Analyzing..."):
            response = model.generate_content(prompt)
        st.subheader("AI Explanation")
        st.write(response.text)

    except Exception:
        st.warning("AI analysis is temporarily unavailable. Please try again later.")
