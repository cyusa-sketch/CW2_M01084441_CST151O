import streamlit as st
from datetime import date
from app.data.incidents import get_all_incidents, create_incident

st.title("Cyber Incident Dashboard")

incidents = get_all_incidents()

if incidents.empty:
    st.info("No incidents found.")
else:
    st.subheader("Recorded Incidents")
    st.dataframe(incidents, use_container_width=True)

    st.subheader("Severity Distribution")
    st.bar_chart(incidents["severity"].value_counts())

st.subheader("Report New Incident")

with st.form("incident_form"):
    incident_type = st.selectbox(
        "Incident Type",
        ["Phishing", "Malware", "DDoS", "Unauthorized Access"]
    )
    severity = st.selectbox("Severity", ["Low", "Medium", "High"])
    status = st.selectbox("Status", ["Open", "In Progress", "Resolved"])
    incident_date = st.date_input("Incident Date", value=date.today())
    description = st.text_area("Description")

    submitted = st.form_submit_button("Submit Incident")

    if submitted:
        if description.strip() == "":
            st.warning("Description cannot be empty.")
        else:
            create_incident(
                incident_type=incident_type,
                severity=severity,
                status=status,
                description=description,
                date=str(incident_date),
                reported_by=st.session_state.get("username", "system")
            )
            st.success("Incident reported successfully.")
            st.rerun()
