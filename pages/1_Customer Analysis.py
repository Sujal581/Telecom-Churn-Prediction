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

page_header("👥 Customer Analysis","Explore customer demographics, behavior patterns, and churn characteristics")

#---Kpis---
male_customers=len(df[df["gender"]=="Male"])
female_customers=len(df[df["gender"]=="Female"])
senior_customers=len(df[df["SeniorCitizen"]==1])
c1,c2,c3,c4=st.columns(4)
kpi_card(c1,"👥 Total Customers",summary["Total Customers"],color="blue")
kpi_card(c2,"👨🏻 Male Customers",male_customers,color="purple")
kpi_card(c3,"👩🏻 Female Customers",female_customers,color="green")
kpi_card(c4,"👴🏻 Senior Customers",senior_customers,color="orange")

#---Visualization---
c1,c2=st.columns(2)
with c1:
    section_header("🚻 Gender Distribution")
    chart_label("📌 Distribution of customers by gender.")
    gender_dist=df["gender"].value_counts().reset_index()
    gender_dist.columns=["Gender","Count"]
    fig=px.pie(gender_dist,names="Gender",values="Count")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: A balanced gender distribution indicates broad market reach, while significant differences may suggest opportunities for targeted marketing campaigns.")

with c2:
    section_header("❌ Churn by Customers")
    chart_label("📌 Comparison of churned and retained customers across gender groups.")
    fig=px.histogram(df,x="gender",color="Churn",barmode="group")
    fig.update_xaxes(title="Gender")
    fig.update_yaxes(title="Count")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Analyzing churn by gender helps identify whether retention strategies need to be tailored for specific customer segments.")

c3,c4=st.columns(2)
with c3:
    section_header("👴🏻 Senior Citizen vs Churn")
    chart_label("📌 Churn distribution among senior and non-senior customers.")
    fig=px.histogram(df,x="SeniorCitizen",color="Churn",barmode="group",color_discrete_sequence=["blue","purple"])
    fig.update_xaxes(title="Senior Citizen")
    fig.update_yaxes(title="Count")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Senior citizens often have different service expectations and usage patterns, making them an important segment for retention analysis.")

with c4:
    section_header("🤝 Partner Status vs Churn")
    chart_label("📌 Churn comparison based on customer partnership status.")
    fig=px.histogram(df,x="Partner",color="Churn",barmode="group",color_discrete_sequence=["orange","cyan"])
    fig.update_xaxes(title="Partner Status")
    fig.update_yaxes(title="Count")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Customers with partners may exhibit stronger retention due to shared household service dependencies and long-term commitments.")

c5,c6=st.columns(2)
with c5:
    section_header("🚩 Dependents vs Churn")
    chart_label("📌 Churn distribution among customers with and without dependents.")
    fig=px.histogram(df,x="Dependents",color="Churn",barmode="group",color_discrete_sequence=["orange","green"])
    fig.update_xaxes(title="Dependents")
    fig.update_yaxes(title="Count")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Customers with dependents may have greater service stability, while those without dependents may be more likely to switch providers.")

with c6:
    section_header("🛑 Churn Rate by Demographic Group")
    chart_label("📌 Churn rate percentage across demographic customer groups.")
    gender_churn=pd.crosstab(df["gender"],df["Churn"],normalize="index")*100
    gender_churn=gender_churn.reset_index()
    fig=px.bar(gender_churn,x="gender",y="Yes",color="gender")
    fig.update_xaxes(title="Gender")
    fig.update_yaxes(title="Count")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Demographic segments with higher churn rates should be prioritized for retention campaigns, personalized offers, and customer engagement initiatives.")

#---Insights---
section_header("💡 Key Insights")
insight_card("👴🏻 Senior citizens show higher churn rate.",kind="info")
insight_card("👥 Customers without partners are more likely to leaves.",kind="warning")
insight_card("❌ Customers with dependents tend to stay longer.",kind="success")
insight_card("🚻 Gender has minimal impact compared to tenure and contract type",kind="error")