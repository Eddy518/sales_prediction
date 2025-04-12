import streamlit as st
from streamlit import session_state as ss
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import time

# Set page title
st.set_page_config(page_title="Logout", page_icon="🚪")

CONFIG_FILENAME = "config.yaml"

# Check if user is logged in first
if "authentication_status" not in ss or not ss["authentication_status"]:
    st.warning("You are not currently logged in.")
    st.info("Redirecting to login page...")
    time.sleep(2)  # Give user time to read the message
    st.switch_page("../streamlit_app.py")
else:
    # Load authentication configuration
    with open(CONFIG_FILENAME) as file:
        config = yaml.load(file, Loader=SafeLoader)

    # Initialize authenticator
    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
        config["preauthorized"],
    )

    # Display logout message
    st.header("Logout")
    st.write(f"You are currently logged in as **{ss.get('name', '')}**")

    # Perform logout
    authenticator.logout("Logout", "main")

    # This will execute only if the logout button wasn't pressed
    # or if logout didn't reset authentication_status
    if not ss.get("authentication_status"):
        st.success("You have been successfully logged out!")
        st.info("Redirecting to login page...")
        time.sleep(2)  # Give user time to read the message
        st.switch_page("../streamlit_app.py")
