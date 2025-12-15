import streamlit as st
from app.services.user_service import login_user

# if the user is already logged in, redirect to dashboard
if st.session_state.get("logged_in", False):
    st.switch_page("pages/Dashboard.py")

st.title("Sign In")

# where the usear enters their credentials
user_val = st.text_input("Enter your username")
pass_val = st.text_input("Enter your password", type="password")

st.page_link("pages/Register.py", label="Need an account? Create one")

# logging in the user
if st.button("Sign In"):
    if not user_val or not pass_val:
        st.error("Please enter both username and password.")
        st.stop()

    okay, feedback = login_user(user_val, pass_val)

    if okay:
        st.session_state["logged_in"] = True
        st.session_state["username"] = user_val
        st.switch_page("pages/Dashboard.py")
    else:
        st.error(feedback)
