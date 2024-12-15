import streamlit as st


def main():
    st.title("Telco Customer Churn App")
    st.write(
        """
        Welcome to the **Telco Customer Churn Prediction App**! This application is designed to 
        help businesses understand customer behavior and predict churn.
    
        ### What is Customer Churn?
        A churn in telco and other subscription-based services means a situation when the 
        customer leaves the service provider.
        
        Churn can result in substantial losses for the organization, as departing customers not only 
        discontinue their service usage but also potentially damage the company's reputation and 
        reduce revenue.
        
        The aim of this app is to **predict which customers are likely to churn**.

        This app utilizes Logistic Regression as its predictive model and employs SMOTEENN as the resampling 
        technique to handle imbalanced target classes. By implementing these methods, the app aims to reduce 
        churn costs by approximately 33%.
    """
    )

    st.subheader("App Features")
    st.write(
        """
        In the sidebar on the left, there is navigation to different sections:
        1. **Data Visualisization**: This section displays the dataset used to train the model, including 
        a count plot for each categorical feature and a histogram for each numerical feature, with "Churn" 
        as the hue.
        2. **Model Evaluation**: This section presents the confusion matrix as a metric for evaluation, 
        along with the precision-recall curve, as the model is more focused on recall as the primary 
        evaluation metric.
        3. **Predict**: In this page, users can input their data features and receive predictions based 
        on the model.
        4. **Predict History**: This section shows the history of predictions made previously, allowing 
        users to review past inputs and results.
    """
    )

    st.subheader("Data Features")
    st.write(
        """
        - Dependents: Whether the customer has dependents or not.
        - Tenure: Number of months the customer has stayed with the company.
        - OnlineSecurity: Whether the customer has online security or not.
        - OnlineBackup: Whether the customer has online backup or not.
        - InternetService: Whether the client is subscribed to Internet service.
        - DeviceProtection: Whether the client has device protection or not.
        - TechSupport: Whether the client has tech support or not 
        - Contract: Type of contract according to duration.
        - PaperlessBilling: Bills issued in paperless form.
        - MonthlyCharges: Amount of charge for service on monthly bases.
        - Churn: Whether the customer churns or not.
    """
    )


if __name__ == "__main__":
    main()
