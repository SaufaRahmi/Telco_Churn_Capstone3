import streamlit as st
import pandas as pd
import seaborn as sns
import pickle
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_curve, PrecisionRecallDisplay

# Load model from pickle file
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


# Load dataset
@st.cache_data
def load_data():
    data = pd.read_csv("./test_data.csv")
    return data


data = load_data()
X_test = data.drop(columns="Churn")
y_test = data["Churn"]

# Predict
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)
y_pred_proba = y_pred_proba[:, 1]

# Show confusion matrix
st.subheader("Confusion Matrix")
fig, ax = plt.subplots()
matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(
    matrix,
    annot=True,
    fmt="d",
    cmap="autumn",
    xticklabels=["Predicted Not Churn", "Predicted Churn"],
    yticklabels=["Actual Not Churn", "Actual Churn"],
    ax=ax,
)
st.pyplot(fig)
st.write(
    """
    Based on the confusion matrix above:
    1. Accuracy = 69.98%
    2. Precision = 46.64%
    3. Recall = 87.07%
    4. F1 Score = 60.74%
"""
)

# Show precision-recall curve
st.subheader("Precision-Recall Curve")
st.write("In this plot, we can see the trade-off between the precision and recall.")
fig, ax = plt.subplots()
precision, recall, thresholds = precision_recall_curve(y_test, y_pred_proba)
PrecisionRecallDisplay(precision, recall).plot(ax=ax)
st.pyplot(fig)
