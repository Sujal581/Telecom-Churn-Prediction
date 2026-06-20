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

page_header("💳 Billing Analysis","Analyze customer billing patterns, payment methods, and revenue-related churn trends")

#---Kpis---
total_revenue=df["TotalCharges"].sum()
avg_monthly=df["MonthlyCharges"].mean()
avg_total=df["TotalCharges"].mean()
mothly_contract=len(df[df["Contract"]=="Month-to-month"])

c1,c2,c3,c4=st.columns(4)
kpi_card(c1,"💵 Total Revenue",f"${total_revenue:,.0f}",color="green")
kpi_card(c2,"🪙 Average Monthly Charges",f"${avg_monthly:.2f}",color="orange")
kpi_card(c3,"💰 Average Total Charges",f"${avg_total:.2f}",color="blue")
kpi_card(c4,"🗓️ Month to Month Contracts",mothly_contract,color="purple")

#---Visualization---
c1,c2,c3=st.columns(3)
with c1:
    section_header("📄 Contract Type Distribution")
    chart_label("📌 Distribution of customers across different contract types.")
    contract_df=df["Contract"].value_counts().reset_index()
    contract_df.columns=["Contract","Count"]
    fig=px.bar(contract_df,x="Contract",y="Count",color="Contract")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Contract type is a key predictor of customer retention. Long-term contracts generally indicate stronger customer commitment and lower churn risk.")

with c2:
    section_header("❌ Churn by Contract Type")
    chart_label("📌 Customer churn distribution across contract categories.")
    fig=px.histogram(df,x="Contract",color="Contract")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Month-to-month contracts often exhibit higher churn levels due to lower switching barriers and reduced customer commitment.")

with c3:
    section_header("💰 Monthly Charge Distribution")
    chart_label("📌 Distribution of customer monthly charges.")
    fig=px.histogram(df,x="MonthlyCharges",nbins=30)
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Understanding pricing distribution helps identify customer segments that may be sensitive to service costs and pricing strategies.")

st.markdown("---")
c4,c5,c6=st.columns(3)
with c4:
    section_header("📊 Monthly Charges vs Churn")
    chart_label("📌 Comparison of monthly charges between churned and retained customers.")
    fig=px.box(df,x="Churn",y="MonthlyCharges",color="Churn")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Customers with higher monthly charges may be more likely to churn if they perceive insufficient value from the services provided.")

with c5:
    section_header("💳 Total Charges vs Churn")
    chart_label("📌 Comparison of total customer spending by churn status.")
    fig=px.box(df,x="Churn",y="TotalCharges",color="Churn")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Higher total charges often indicate long-term customer relationships, while lower total charges may signal recently acquired customers with greater churn risk.")

with c6:
    section_header("💸 Payment Methods")
    chart_label("📌 Customer distribution by payment method and churn status.")
    fig=px.histogram(df,x="PaymentMethod",color="Churn",barmode="group")
    fig.update_layout(xaxis_title="Payment Method",yaxis_title="Customers")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Payment preferences can reveal behavioral patterns, with certain payment methods often associated with higher customer turnover.")

st.markdown("---")
c7,c8,c9=st.columns(3)
with c7:
    section_header("📊 Paperless Billing vs Churn")
    chart_label("📌 Churn comparison between customers using and not using paperless billing.")
    fig=px.histogram(df,x="PaperlessBilling",color="Churn",barmode="group")
    fig.update_layout(xaxis_title="Paperless Billing",yaxis_title="Customers")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Paperless billing adoption may correlate with customer behavior patterns that influence retention and service engagement.")

with c8:
    section_header("📈 Churn Rate by Contract (%)")
    chart_label("📌 Churn rate percentage for each contract type.")
    contract_churn = (pd.crosstab(df["Contract"],df["Churn"],normalize="index") * 100)
    contract_churn = (contract_churn["Yes"].reset_index())
    fig = px.bar(contract_churn,x="Contract",y="Yes",text_auto=".1f",color="Contract")
    apply_plot_layout(fig)
    st.plotly_chart(fig, use_container_width=True)
    chart_note("💡 Chart Note: Contract categories with elevated churn rates should be prioritized for targeted retention programs and loyalty initiatives.")

with c9:
    section_header("📉 Churn Rate by Payment Method")
    chart_label("📌 Churn rate percentage across payment methods.")
    payment_churn = (pd.crosstab(df["PaymentMethod"],df["Churn"],normalize="index") * 100)
    payment_churn = (payment_churn["Yes"].reset_index())
    fig = px.bar(payment_churn,x="PaymentMethod",y="Yes",text_auto=".1f",color="PaymentMethod")
    apply_plot_layout(fig)
    st.plotly_chart(fig, use_container_width=True)
    chart_note("💡 Chart Note: Identifying payment methods associated with higher churn enables businesses to design more effective customer retention strategies.")

section_header("🎯 HIGH-RISK BILLING SEGMENTS")
chart_label("📌 Customer billing segments identified as having elevated churn risk.")
high_risk = pd.DataFrame({
    "Segment": [
        "Month-to-Month Contract",
        "High Monthly Charges",
        "Electronic Check Users",
        "Paperless Billing Customers"
    ],
    "Risk Level": [
        "High",
        "High",
        "Medium",
        "Medium"
    ],
    "Reason": [
        "Less commitment and higher churn tendency",
        "Customers may switch due to pricing concerns",
        "Often associated with higher churn rates",
        "Common among churn-prone customer groups"
    ]
})
st.dataframe(high_risk, use_container_width=True)
chart_note("Billing-related factors such as short-term contracts, high monthly costs, and specific payment methods significantly influence churn behavior. These segments should be targeted with personalized pricing plans, loyalty incentives, and retention-focused campaigns.")

#---Insights---
st.subheader("💡 Key Insights")
insight_card("🗓️ Month-to-month customers show the highest churn risk.",kind="warning")
insight_card("📈 Long-term contracts significantly improve retention.",kind="success")
insight_card("👨🏻 Customers with high monthly charges are more likely to leave.",kind="error")
insight_card("💳 Electronic check users often exhibit higher churn rates.",kind="info")
insight_card("📝 Contract upgrades can be an effective retention strategy.",kind="cyan")