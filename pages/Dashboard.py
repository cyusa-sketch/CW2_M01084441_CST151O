import streamlit as st

# restrict access to logged-in users only
logged = st.session_state.get("logged_in", False)

if not logged:
    # If someone tries to open the dashboard manually, send them back
    st.switch_page("pages/Login.py")

# Display the user info who logged in on the dashboard
user_name = st.session_state.get("username", "Guest")

st.title("User Dashboard")
st.caption("You’re currently signed in to your account.")

st.markdown(f"### Hello, **{user_name}**!")
st.write("This is your main dashboard area.")

# the oti
if st.button("Sign Out"):
    st.session_state["logged_in"] = False
    st.session_state["username"] = None
    st.switch_page("pages/Login.py")
