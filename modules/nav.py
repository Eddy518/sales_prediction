import streamlit as st
from streamlit import session_state as ss


def HomeNav():
    st.sidebar.page_link("streamlit_app.py", label="Home", icon="🏠")


def LoginNav():
    st.sidebar.page_link("./pages/account.py", label="Account", icon="🔐")


def SalesPredictorNav():
    st.sidebar.page_link(
        "./pages/sales_predictor.py", label="Sales Predictor", icon="📈"
    )


def MenuButtons(user_roles=None):
    if user_roles is None:
        user_roles = {}

    if "authentication_status" not in ss:
        ss.authentication_status = False

    # Always show the home and login navigators.
    HomeNav()
    LoginNav()

    # Show the other page navigators depending on the users' role.
    if ss["authentication_status"]:
        SalesPredictorNav()
