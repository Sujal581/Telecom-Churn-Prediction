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

page_header("📡 Service Analysis","Analyze service subscriptions, usage patterns, and their impact on customer churn")

#---Kpis---
internet_users=len(df[df["InternetService"]!="No"])
tech_support=len(df[df["TechSupport"]=="Yes"])
online_security=len(df[df["OnlineSecurity"]=="Yes"])
streaming_user=len(df[(df["StreamingTV"]=="Yes") | (df["StreamingMovies"]=="Yes")])
c1,c2,c3,c4=st.columns(4)

kpi_card(c1,"🌐 Internet Users",internet_users,color="blue")
kpi_card(c2,"🛠️ Tech Support User",tech_support,color="purple")
kpi_card(c3,"🔒 Online Security Users",online_security,color="orange")
kpi_card(c4,"📺 Streaming Users",streaming_user,color="red")

#---Visualization---
c1,c2,c3=st.columns(3)
with c1:
    section_header("🌐 Internet Service Distribution")
    chart_label("📌 Distribution of customers across different internet service types.")
    fig=px.pie(df,names="InternetService")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Understanding service adoption helps identify the most popular internet offerings and supports infrastructure planning.")

with c2:
    section_header("❌ Churn by Internet Service")
    chart_label("📌 Comparison of churned and retained customers across internet service categories.")
    fig=px.histogram(df,x="InternetService",color="Churn",barmode="group")
    fig.update_xaxes(title="Internet Service")
    fig.update_yaxes(title="Count")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Certain internet services may exhibit higher churn rates, indicating potential service quality or pricing concerns.")

with c3:
    section_header("🔒 Online Security vs Churn")
    chart_label("📌 Customer churn distribution based on online security subscription status.")
    fig=px.histogram(df,x="OnlineSecurity",color="Churn",barmode="group",color_discrete_sequence=["orange","green"])
    fig.update_xaxes(title="Online Security")
    fig.update_yaxes(title="Count")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Customers without online security services tend to show higher churn propensity, highlighting the value of security-related offerings.")

st.markdown("---")
c4,c5,c6=st.columns(3)
with c4:
    section_header("⚙️ Tech Support vs Churn")
    chart_label("📌 Churn comparison between customers with and without technical support.")
    fig=px.histogram(df,x="TechSupport",color="Churn",barmode="group",color_discrete_sequence=["blue","purple"])
    fig.update_xaxes(title="Tech Support")
    fig.update_yaxes(title="Count")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Access to technical support can improve customer satisfaction and contribute to stronger retention rates.")

with c5:
    section_header("💾 Online Backup vs Churn")
    chart_label("📌 Churn distribution by online backup service subscription.")
    fig=px.histogram(df,x="OnlineBackup",color="Churn",barmode="group",color_discrete_sequence=["blue","red"])
    fig.update_xaxes(title="Online Backup")
    fig.update_yaxes(title="Count")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Customers utilizing backup services are often more engaged with the company's ecosystem and may be less likely to churn.")

with c6:
    section_header("📱 Device Protection vs Churn")
    chart_label("📌 Churn behavior among customers with and without device protection services.")
    fig=px.histogram(df,x="DeviceProtection",color="Churn",barmode="group",color_discrete_sequence=["green","red"])
    fig.update_xaxes(title="Device Protection")
    fig.update_yaxes(title="Count")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Device protection plans can increase perceived service value and encourage long-term customer retention.")

st.markdown("---")
c7,c8,c9=st.columns(3)
with c7:
    section_header("📺 Streaming TV vs Churn")
    chart_label("📌 Churn comparison based on streaming TV service adoption.")
    fig=px.histogram(df,x="StreamingTV",color="Churn",barmode="group",color_discrete_sequence=["orange","red"])
    fig.update_xaxes(title="Streaming TV")
    fig.update_yaxes(title="Count")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Entertainment-focused services can enhance customer engagement and reduce the likelihood of switching providers.")

with c8:
    section_header("🎥 Streaming Movie vs Churn")
    chart_label("📌 Distribution of churned and retained customers by streaming movie subscription.")
    fig=px.histogram(df,x="StreamingMovies",color="Churn",barmode="group",color_discrete_sequence=["blue","cyan"])
    fig.update_xaxes(title="Streaming Movies")
    fig.update_yaxes(title="Count")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Bundled streaming services may strengthen customer loyalty by increasing overall service utilization.")

with c9:
    service_col=["OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport"]
    service_churn=[]
    for col in service_col:
        churn_rate=pd.crosstab(df[col],df["Churn"],normalize="index")*100
        if "Yes" in churn_rate.index:
            service_churn.append({"Service":col,"Churn Rate":round(churn_rate.loc["Yes","Yes"],2)})
    service_df=pd.DataFrame(service_churn)

    section_header("🚩 Churn Rate by Services (%)")
    chart_label("📌 Churn rate percentage among customers subscribed to value-added services.")
    fig=px.bar(pd.DataFrame(service_churn),x="Service",y="Churn Rate",color="Service")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("💡 Chart Note: Services with lower churn rates indicate stronger customer engagement and can be leveraged in retention-focused marketing strategies.")

section_header("🗒️ High Risk Service Groups")
c10,c11=st.columns(2)
with c10:
    chart_label("📌 High-Risk Service Groups by Churn Rate")
    high_risk = pd.DataFrame({
        "Group": [
            "No Tech Support",
            "No Online Security",
            "Fiber Optic Users",
            "No Device Protection"
        ],
        "Churn Rate (%)": [
            round(df[df["TechSupport"]=="No"]["Churn"].eq("Yes").mean()*100,2),
            round(df[df["OnlineSecurity"]=="No"]["Churn"].eq("Yes").mean()*100,2),
            round(df[df["InternetService"]=="Fiber optic"]["Churn"].eq("Yes").mean()*100,2),
            round(df[df["DeviceProtection"]=="No"]["Churn"].eq("Yes").mean()*100,2)
        ]
    })

    high_risk["Risk Level"] = high_risk["Churn Rate (%)"].apply(lambda x: "🔴 High" if x >= 40 else "🟡 Medium" if x >= 25 else "🟢 Low")
    st.dataframe(high_risk.sort_values("Churn Rate (%)",ascending=False),use_container_width=True)

with c11:
    fig = px.bar(high_risk.sort_values("Churn Rate (%)"),x="Churn Rate (%)",y="Group",orientation="h",text="Churn Rate (%)",color="Churn Rate (%)")
    st.plotly_chart(fig, height=270)
chart_note("Customers without Tech Support, Online Security, or Device Protection generally exhibit higher churn rates. Fiber Optic users may also require targeted retention strategies due to elevated churn risk.")

#---Insights---
section_header("💡 Key Insights")
insight_card("👥 Customers without Tech Support Churn significantly more.",kind="warning")
insight_card("🌐 Online Security is associated with better customer retention.",kind="success")
insight_card("🔌 Fiber Optic Customers may experience higher churn.",kind="cyan")
insight_card(" 📞 Customers using multiple services tend to stay longer.")
insight_card("📦 Service Bundle can be used as retention offer.",kind="success")