import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder

@st.cache_data
def load_data(file):
    df=pd.read_csv(file)
    return df

@st.cache_data
def clean_data(df):
    if "customerID" in df.columns:
        df=df.drop("customerID",axis=1)
        df["TotalCharges"]=pd.to_numeric(df["TotalCharges"],errors="coerce")
        df["TotalCharges"]=df["TotalCharges"].fillna(df["TotalCharges"].median())
    return df
    
@st.cache_data
def encode_data(df):
    df_encoded=df.copy()
    label_encoders={}
    categorical_cols=df_encoded.select_dtypes(include="object").columns
    for col in categorical_cols:
        le=LabelEncoder()
        df_encoded[col]=le.fit_transform(df_encoded[col])
        label_encoders[col]=le
    return df_encoded, label_encoders


@st.cache_data
def churn_summary(df):
    total_customers = len(df)
    churned = len(df[df["Churn"] == "Yes"])
    active = total_customers - churned
    churn_rate = (churned / total_customers * 100)
    avg_tenure = df["tenure"].mean()
    avg_monthly = df["MonthlyCharges"].mean()
    return {
        "Total Customers": total_customers,
        "Active Customers": active,
        "Churned Customers": churned,
        "Churn Rate": round(churn_rate, 2),
        "Avg Tenure": round(avg_tenure, 1),
        "Avg Monthly Charges": round(avg_monthly, 2)
    }

@st.cache_data
def feature_importance(model,X):
    importance_df=pd.DataFrame({"Feature":X.columns,"Importance":model.feature_importances_})
    return (importance_df.sort_values(by="Importance",ascending=False))

@st.cache_data
def risk_category(probability):
    if probability < 0.30:
        return "🟡 Low Risk"
    elif probability < 0.60:
        return "🟠 Medium Risk"
    else:
        return "🟤 High Risk"