import streamlit as st
from app.data.db import connect_database
from app.data.schema import create_all_tables

# connect to the database and ensure all tables exist
conn = connect_database()
create_all_tables(conn)
conn.close()

# the main navigation bar
nav = st.navigation(
    [
        st.Page("pages/Login.py", title="Login"),
        st.Page("pages/Register.py", title="Register"),
        st.Page("pages/Dashboard.py", title="Dashboard"),
        st.Page("pages/Cyber.py", title="Cyber View"),
        st.Page("pages/Analyzer.py", title="AI Analyzer"),
    ]
)

st.sidebar.page_link("pages/Dashboard.py", label="Dashboard")
st.sidebar.page_link("pages/Cyber.py", label="Cyber View")
st.sidebar.page_link("pages/Analyzer.py", label="AI Analyzer")

nav.run()
