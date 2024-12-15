import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load dataset
@st.cache_data
def load_data():
    data = pd.read_csv("./data_telco_customer_churn.csv")
    return data


data = load_data()

# Show data
st.title("Telco Customer Churn Data Visualization")
st.write("Table of the dataset used to create the Telco Customer Churn app model")
st.write(data)

# Show countplot for categorical data
st.subheader("Countplot for Categorical Data")
categorical_columns = data.select_dtypes(
    include=["object", "category"]
).columns.tolist()
selected_categorical = st.selectbox("Choose categorical column:", categorical_columns)

if selected_categorical:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x=selected_categorical, hue="Churn")
    plt.title(f"Countplot for {selected_categorical} with Churn Hue")
    st.pyplot(plt)

# Show histplot for numerical data
st.subheader("Histplot untuk Data Numerikal")
numerical_columns = data.select_dtypes(include=["float64", "int64"]).columns.tolist()
selected_numerical = st.selectbox("Choose numerical column:", numerical_columns)

if selected_numerical:
    plt.figure(figsize=(10, 6))
    sns.histplot(
        data=data, x=selected_numerical, hue="Churn", multiple="stack", kde=True
    )
    plt.title(f"Histplot for {selected_numerical} with Churn Target")
    st.pyplot(plt)

# Show pie chart for 'Churn'
st.subheader("Churn Pie Chart")
st.write("Figure of Churn Distribution using Pie Chart")
churn_counts = data["Churn"].value_counts()
plt.figure(figsize=(2, 2))
plt.pie(
    churn_counts,
    labels=churn_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#ff9999", "#66b3ff"],
    textprops={"fontsize": 5},
)
plt.title("Churn Distribution", fontsize=7)
plt.axis("equal")
st.pyplot(plt, use_container_width=False)
