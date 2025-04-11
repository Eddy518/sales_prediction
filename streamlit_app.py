import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons
from pages.account import get_roles

# If the user reloads or refreshes the page while still logged in,
# go to the account page to restore the login status. Note reloading
# the page changes the session id and previous state values are lost.
# What we are doing is only to relogin the user.
if "authentication_status" not in ss:
    st.switch_page("./pages/account.py")

st.markdown(
    """
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""",
    unsafe_allow_html=True,
)

MenuButtons(get_roles())
st.header("Home page")


# Protected content in home page.
if ss.authentication_status:
    st.markdown("### How to Use the Sales Predictor")
    st.markdown(
        """
    To use our sales prediction tool:

    1. **Click on "Sales Predictor" in the sidebar** 📈
    2. Adjust the sliders to set your product price, advertising budget, and promotion budget
    3. Click the "Click to predict unit sales" button
    4. View your predicted sales results instantly!

    The Sales Predictor uses machine learning to estimate how different price points and marketing strategies will affect your sales volume.
    """
    )

    st.info(
        "📊 Try different combinations of price and marketing budgets to find your optimal sales strategy!"
    )
else:
    # Hide deprecation warnings
    # st.set_option("deprecation.showfileUploaderEncoding", False)
    # st.set_option("deprecation.showPyplotGlobalUse", False)

    # Login message at the top
    st.info(
        "👋 **Please log in or register (by clicking on Account) to access the full features of our prediction system.**"
    )

    st.markdown("### 🚀 Welcome to the Sales Prediction System")

    st.image(
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80",
        caption="Sales Analytics Dashboard",
        use_column_width=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📊 Predict Your Future Sales")
        st.markdown(
            """
        Our advanced sales prediction system helps you:
        * Forecast upcoming sales trends
        * Identify growth opportunities
        * Plan inventory efficiently
        * Optimize your marketing budget
        """
        )

    with col2:
        st.markdown("#### 🧮 How It Works")
        st.markdown(
            """
        We use powerful **regression models** to analyze:
        * Historical sales data
        * Seasonal patterns
        * Market variables
        * Consumer behavior

        Our algorithms find hidden patterns in your data!
        """
        )

    st.markdown("---")
    st.markdown("#### Why Choose Our System?")
    metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
    metrics_col1.metric("Prediction Accuracy", "94.3%", "2.1%")
    metrics_col2.metric("Processing Time", "0.5s", "-0.2s")
    metrics_col3.metric("Satisfied Users", "2,543", "+89")
