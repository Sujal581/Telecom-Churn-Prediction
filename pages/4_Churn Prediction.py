import pandas as pd
import plotly.express as px
import streamlit as st
import joblib
from utils import *
from style import *

st.set_page_config(
    page_title="Telecom Churn Dashboard",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="expanded"
)

df=load_data("churn.csv")
df=clean_data(df)
summary=churn_summary(df)
inject_css()
sidebar_brand()

page_header("🤖 Churn Prediction","Predict customer churn risk using Machine Learning.")

#--- LOAD MODEL---
model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")

#--- INPUT FORM---
section_header("📋 Customer Information")
col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("Gender",["Female", "Male"])
    senior = st.selectbox("Senior Citizen",["No", "Yes"])
    partner = st.selectbox("Partner",["No", "Yes"])
    dependents = st.selectbox("Dependents",["No", "Yes"])
    tenure = st.slider("Tenure (Months)",0,72,12)

with col2:
    internet = st.selectbox("Internet Service",["DSL", "Fiber optic", "No"])
    tech_support = st.selectbox("Tech Support",["No", "Yes"])
    security = st.selectbox("Online Security",["No", "Yes"])
    contract = st.selectbox("Contract",["Month-to-month","One year","Two year"])
    monthly = st.slider("Monthly Charges",0.0,150.0,70.0)

#--- PREDICT BUTTON---
if st.button("🔮 Predict Churn"):
    input_data = pd.DataFrame({
        "gender":[1 if gender=="Male" else 0],
        "SeniorCitizen":[1 if senior=="Yes" else 0],
        "Partner":[1 if partner=="Yes" else 0],
        "Dependents":[1 if dependents=="Yes" else 0],
        "tenure":[tenure],
        "PhoneService":[1],
        "MultipleLines":[0],
        "InternetService":[2 if internet=="Fiber optic" else 1 if internet=="DSL" else 0],
        "OnlineSecurity":[1 if security=="Yes" else 0],
        "OnlineBackup":[0],
        "DeviceProtection":[0],
        "TechSupport":[1 if tech_support=="Yes" else 0],
        "StreamingTV":[0],
        "StreamingMovies":[0],
        "Contract":[0 if contract=="Month-to-month" else 1 if contract=="One year" else 2],
        "PaperlessBilling":[1],
        "PaymentMethod":[0],
        "MonthlyCharges":[monthly],
        "TotalCharges":[tenure * monthly]
    })
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    st.divider()
    section_header("📊 Prediction Results")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Churn Probability",f"{probability*100:.1f}%")

    with col2:
        if probability < 0.40:
            risk = "🟢 Low Risk"
        elif probability < 0.70:
            risk = "🟡 Medium Risk"
        else:
            risk = "🔴 High Risk"
        st.metric("Risk Level",risk)

    #--- ALERT---
    if prediction == 1:
        st.error("⚠️ This customer is likely to churn.")
    else:
        st.success("✅ This customer is likely to stay.")

    #--- RETENTION RECOMMENDATION---
    section_header("💡 Retention Recommendations")
    recommendations = []
    if contract == "Month-to-month":recommendations.append("Offer a long-term contract discount.")
    if tech_support == "No":recommendations.append("Provide a free Tech Support trial.")
    if security == "No":recommendations.append("Offer Online Security services.")
    if monthly > 80:recommendations.append("Provide loyalty discounts.")
    if tenure < 12:recommendations.append("Enroll customer in a welcome retention program.")
    if recommendations:
        for rec in recommendations:
            st.info(rec)
    else:
        st.success("No immediate retention action required.")