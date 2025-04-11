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

MenuButtons(get_roles())
st.header("Sales Predictor")

# Imports
import streamlit as st
import pandas as pd
import pickle

# setting the basic configuration of the web app. This is shown in the Tab
# st.set_page_config(page_title="Sales Prediction", page_icon=":bar_chart:")

# Opening intro text
st.write("# Predict Sales✨")

with st.expander("About this app"):

    st.write("")

    st.markdown(
        """

    This is a simulated dataset for a Case Study to demonstrate the usage of Linear Regression to solve business problem.

    The data spans 24 months and has `unit sales` along with the `price`, `advertisment spend` and `promotion spend`

    The predictions are based on a Linear Regression model . It is used to establish the relationship between the independent variables (price, promotion and advertisment) to predict the unit sales for each given scenario.

    """
    )

st.write("### Determine the scenario 🎛️:")

# Price of the product
price = st.slider(
    "💲 Price of the product?", min_value=1, max_value=15, value=7, step=1
)

# Advertisment budget
ads = st.slider(
    "📢 What is the Adv budget?", min_value=35, max_value=65, value=50, step=1
)


# Promotions
promo = st.slider(
    "💥 What is the promotional budget?", min_value=35, max_value=65, value=45, step=1
)


# Creating the dataframe to run predictions on
row = [price, ads, promo]
columns = ["dollar_price", "advertisment", "promotions"]

mktg_scenario = pd.DataFrame(dict(zip(columns, row)), index=[0])

# Show the table?
st.table(mktg_scenario)

# Now predicting!
if st.button(label="Click to predict unit sales"):

    # Load the model
    loaded_model = pickle.load(open("./model/lm_model_prediction.sav", "rb"))

    # Make predictions (and get out pred probabilities)
    pred = loaded_model.predict(mktg_scenario)[0]

    st.write(f"Predicted Unit Sales💰: {pred:,.0f} units ")
