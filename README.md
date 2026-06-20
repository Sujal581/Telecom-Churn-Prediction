# 📞 Telecom Customer Churn Prediction & Retention Analytics using Machine Learning

## 📌 Project Overview

Customer churn is one of the most critical challenges faced by telecom companies. Retaining existing customers is significantly more cost-effective than acquiring new ones. This project leverages Machine Learning and Business Intelligence techniques to predict customer churn, identify key churn drivers, and provide actionable retention strategies through an interactive Streamlit dashboard.

The solution combines Exploratory Data Analysis (EDA), Predictive Modeling, and Retention Analytics to help telecom businesses proactively reduce customer attrition.

---

## 🎯 Objectives

* Analyze customer demographics, services, and billing behavior.
* Identify factors contributing to customer churn.
* Build a Machine Learning model to predict churn risk.
* Segment customers into Low, Medium, and High Risk categories.
* Provide business recommendations for customer retention.
* Deliver insights through an interactive Streamlit dashboard.

---

## 📊 Dashboard Modules

### 🏠 Executive Overview

* Total Customers
* Churn Rate
* Active Customers
* Average Monthly Charges
* Customer Tenure Analysis
* Key Business Insights

### 📊 Customer Analysis

* Gender Distribution
* Senior Citizen Analysis
* Partner & Dependents Analysis
* Demographic Churn Patterns

### 📞 Service Analysis

* Internet Service Analysis
* Online Security Impact
* Tech Support Impact
* Streaming Services Analysis
* High-Risk Service Segments

### 💳 Billing Analysis

* Contract Type Distribution
* Monthly Charges Analysis
* Payment Method Analysis
* Paperless Billing Analysis
* Revenue Risk Assessment

### 🤖 Churn Prediction

* Real-Time Customer Churn Prediction
* Churn Probability Score
* Risk Classification
* Retention Recommendations

### 🎯 Retention Analytics

* Customer Risk Segmentation
* High-Risk Customer Identification
* Revenue at Risk
* Retention Opportunity Analysis

---

## 🤖 Machine Learning

### Target Variable

* Churn (Yes / No)

### Models Evaluated

* Logistic Regression
* Decision Tree
* Random Forest Classifier
* XGBoost (Optional)

### Final Model

* Random Forest Classifier

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score

---

## 📂 Dataset Features

### Customer Information

* gender
* SeniorCitizen
* Partner
* Dependents

### Customer Loyalty

* tenure

### Services

* PhoneService
* MultipleLines
* InternetService
* OnlineSecurity
* OnlineBackup
* DeviceProtection
* TechSupport
* StreamingTV
* StreamingMovies

### Billing Information

* Contract
* PaperlessBilling
* PaymentMethod
* MonthlyCharges
* TotalCharges

### Target

* Churn

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Plotly
* Scikit-Learn
* Joblib
* Matplotlib

---

## 📁 Project Structure

```text
Telecom_Churn/
│
├── app.py
├── telecom_churn.csv
├── model.pkl
├── encoders.pkl
├── utils.py
├── requirements.txt
│
├── pages/
│   ├── 1_Overview.py
│   ├── 2_Customer_Analysis.py
│   ├── 3_Service_Analysis.py
│   ├── 4_Billing_Analysis.py
│   ├── 5_Churn_Prediction.py
│   └── 6_Retention_Analytics.py
│
└── train_model.py
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
cd Telecom_Churn
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📈 Key Insights

* Month-to-Month contracts exhibit the highest churn rates.
* Customers without Tech Support and Online Security are more likely to churn.
* Higher Monthly Charges are associated with increased churn risk.
* Long-tenure customers demonstrate stronger loyalty.
* Retention strategies can significantly reduce customer attrition.

---

## 🎯 Business Impact

This project helps telecom companies:

* Identify customers likely to churn.
* Reduce customer attrition.
* Improve customer retention strategies.
* Increase customer lifetime value.
* Enhance data-driven decision-making.

---

## 👨‍💻 Author

**Sujal**
---

⭐ If you found this project useful, consider giving it a star on GitHub!
