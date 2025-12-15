import streamlit as st
from app.services.user_service import register_user
import re

# Redirect logged-in users to dashboard
if st.session_state.get("logged_in", False):
    st.switch_page("pages/Dashboard.py")

st.title("Create Account")

# Input fields (DESIGN UNCHANGED)
new_user = st.text_input("Choose a username")
new_pass = st.text_input("Create a strong password", type="password")

# Link back to login (DESIGN UNCHANGED)
st.page_link("pages/Login.py", label="Already registered? Sign in instead")


# Password strength validation (logic only, no UI change)
def password_is_valid(p: str):
    if len(p) < 8:
        return False, "Password must be at least **8 characters** long."
    if " " in p:
        return False, "Password cannot contain **spaces**."
    if not re.search(r"[A-Z]", p):
        return False, "Password must contain at least **one uppercase letter (A-Z)**."
    if not re.search(r"[a-z]", p):
        return False, "Password must contain at least **one lowercase letter (a-z)**."
    if not re.search(r"[0-9]", p):
        return False, "Password must include at least **one number (0-9)**."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-\=\+\[\]/\\;']", p):
        return False, "Password must include at least **one special character**."
    return True, ""


# Registration action
if st.button("Register"):
    if not new_user or not new_pass:
        st.error("All fields are required.")
        st.stop()

    strong, msg = password_is_valid(new_pass)
    if not strong:
        st.error(msg)
        st.stop()

    ok, feedback = register_user(new_user, new_pass)

    if ok:
        st.session_state["logged_in"] = True
        st.session_state["username"] = new_user
        st.switch_page("pages/Dashboard.py")
    else:
        st.error(feedback)
