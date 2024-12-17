# Telco Customer Prediction using Machine Learning

In this file, include the csv dataset, machine learning modelling in jupyter notebook, streamlit for visualization, and uploading the dataset and the model into google cloud.

# Business Problem and Data Understanding

**Context:**
The dataset represents customer profiles who have left the telco company. A churn in telco and other subscription-based services means a situation when the customer leaves the service provider. 

**Features:**
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

**Target:**

0 : Customer not churns

1 : Customer churns

**Background**

In the telecommunications industry, customer churn is one of the most significant challenges faced by companies. Churn can result in substantial losses for the organization, as departing customers not only discontinue their service usage but also potentially damage the company's reputation and reduce revenue.

In this context, a telecommunications company possesses a dataset that records the profiles of customers who have left the company. This dataset contains information about customer characteristics, such as whether they have dependents, their tenure as customers, and whether they have subscribed to online security, online backup, internet service, device protection, and technical support, as well as the type of contract they hold.

**Problem Statement**

Based on the available dataset, the telecommunications company aims to **predict which customers are likely to churn** (discontinue their service usage) in the future. By doing so, the company can take proactive measures to prevent customer loss and enhance customer loyalty.

**Confusion Matrix**

- False Positive (FP) occurs when the prediction model incorrectly predicts that a customer will churn, resulting in unnecessary expenses and potential damage to customer relationships.
- False Negative (FN) occurs when the prediction model incorrectly predicts that a customer will not churn, resulting in the loss of that customer and missed opportunities to increase loyalty and retention.

In the context of churn prediction, **False Negative (FN) is more important than False Positive (FP)**. This is because False Negative can result in the loss of customers who actually churn, leading to greater losses for the company. Therefore, reducing the number of False Negative (FN) might be seen as more important.

**Metric Evaluation**: Recall will be used as the primary evaluation metric to compare and select the best model for this project, as our main focus is on minimizing False Negatives (FN) to ensure accurate churn prediction.

# Conlusion

Through various machine learning techniques and hyperparameter iterations conducted to predict customer churn, the Logistic Regression model with initial hyperparameter tuning emerged as the most cost-effective solution. By utilizing this model, customer churn costs can be reduced by up to 33% compared to the assumption that all customers are considered to churn. Based on the classification report above, it can be concluded that the Logistic Regression model used is capable of reducing the number of customers likely to churn by 87% (based on its recall results).
