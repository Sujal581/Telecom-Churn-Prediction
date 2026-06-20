import pandas as pd
import plotly.express as px
import streamlit as st
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

page_header("📊 Telecom Churn Overview","Comprehensive view of customer retention, churn trends, and key business metrics")

#---Kpis---
section_header("📊 Churn Overview")
c1,c2,c3,c4=st.columns(4)
kpi_card(c1,"👥 Total Customers",summary["Total Customers"],color="blue")
kpi_card(c2,"❌ Churned Customers",summary["Churned Customers"],color="red")
kpi_card(c3,"📉 Churn rate",f"{summary['Churn Rate']:.2f}%",color="orange")
kpi_card(c4,"💰 Average Monthly Charges",f"${summary['Avg Monthly Charges']:.2f}",color="green")

#---Visualization---
c1,c2=st.columns(2)
with c1:
    section_header("📉 Churn Distribution")
    chart_label("📌 Distribution of churned and retained customers")
    fig=px.pie(df,names="Churn")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: A higher churn percentage indicates customer retention issues that require immediate attention.")

with c2:
    section_header("📈 Contract Type Distribution")
    chart_label("📌 Number of customers by contract type.")
    contract = df["Contract"].value_counts().reset_index(name="Count")
    contract.columns = ["Contract", "Count"]
    fig=px.bar(contract,x="Contract",y="Count",color="Contract")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Long-term contracts usually have lower churn rates compared to month-to-month contracts.")

c3,c4=st.columns(2)
with c3:
    section_header("🚨 Churn by Contract")
    chart_label("📌 Churn comparison across contract types.")
    fig=px.histogram(df,x="Contract",color="Churn",barmode="group")
    fig.update_xaxes(title="Contract")
    fig.update_yaxes(title="Count")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Customers on month-to-month contracts are generally more likely to churn.")

with c4:
    section_header("⏳ Tenure Distribution")
    chart_label("📌 Customer tenure distribution segmented by churn status.")
    fig=px.histogram(df,x="tenure",nbins=30,color="Churn")
    fig.update_xaxes(title="Tenure")
    fig.update_yaxes(title="Count")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Customers with shorter tenure often show a higher likelihood of churn.")

c6,c7=st.columns(2)
with c6:
    section_header("🗓️ Monthly Charge Distribution")
    chart_label("📌 Distribution of monthly charges among customers.")
    fig=px.histogram(df,x="MonthlyCharges",color="Churn")
    fig.update_xaxes(title="Monthly Charges")
    fig.update_yaxes(title="Count")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Higher monthly charges may contribute to increased churn risk if customers perceive low value.")

with c7:
    section_header("📅 Churn vs Monthly Charges")
    chart_label("📌 Monthly charges comparison between churned and retained customers.")
    fig=px.box(df,x="Churn",y="MonthlyCharges",color="Churn")
    fig.update_xaxes(title="Churn")
    fig.update_yaxes(title="Monthly Charges")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Significant differences in monthly charges can indicate pricing-related churn behavior.")

#---Insights---
section_header("💡 Key Insights")
insight_card("🗓️ Month - to - Month Customers show the highest churn.",kind="info")
insight_card("👥 Customers with longer tenure are more likely to stay.",kind="success")
insight_card("❌ Higher monthly charges are associated with increased churn risk.",kind="warning")
insight_card("🌐 Customers using Tech Support and Online Security Churn are less frequently.",kind="error")
