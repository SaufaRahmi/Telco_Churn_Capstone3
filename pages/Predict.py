import streamlit as st
import pandas as pd
import pickle
from pages.Predict_History import show_history

# Load model from pickle file
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Initialize session state for prediction history
if "predicthistory" not in st.session_state:
    st.session_state.predicthistory = []

# Define the UI for new data input
st.title("Predict Customer Churn")

# Collect user inputs for features
dependents = st.selectbox("Dependents:", ["Yes", "No"])
tenure = st.slider("Tenure:", min_value=0, max_value=72, value=1)
online_security = st.selectbox("Online Security:", ["Yes", "No", "No internet service"])
online_backup = st.selectbox("Online Backup:", ["Yes", "No", "No internet service"])
internet_service = st.selectbox("Internet Service:", ["DSL", "Fiber optic", "No"])
device_protection = st.selectbox("Device Protection:", ["Yes", "No"])
tech_support = st.selectbox("Tech Support:", ["Yes", "No", "No internet service"])
contract = st.selectbox("Contract:", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.selectbox("Paperless Billing:", ["Yes", "No"])
monthly_charges = st.number_input(
    "Monthly Charges:", min_value=18.8, max_value=118.65, value=50.0
)

# Make prediction
if st.button("Predict"):
    # Create a dictionary from user inputs
    input_data = {
        "Dependents": [dependents],
        "tenure": [tenure],
        "OnlineSecurity": [online_security],
        "OnlineBackup": [online_backup],
        "InternetService": [internet_service],
        "DeviceProtection": [device_protection],
        "TechSupport": [tech_support],
        "Contract": [contract],
        "PaperlessBilling": [paperless_billing],
        "MonthlyCharges": [monthly_charges],
    }
    # Create a DataFrame from the input dictionary
    input_df = pd.DataFrame(input_data)

    # Adjust dependants and paperless billing data
    input_df["Dependents"] = input_df["Dependents"].apply(
        lambda data: 1 if data == "Yes" else 0
    )
    input_df["PaperlessBilling"] = input_df["PaperlessBilling"].apply(
        lambda data: 1 if data == "Yes" else 0
    )

    # Predict
    prediction = model.predict(input_df)

    # Store the prediction in session state
    result = "Yes" if prediction[0] == 1 else "No"
    entry = {**input_data, "Churn": result}  # Merge input_data with the result
    st.session_state.predicthistory.append(entry)

    display = (
        "This customer is likely to churn."
        if prediction[0] == 1
        else "This customer is not likely to churn."
    )
    st.write(display)
