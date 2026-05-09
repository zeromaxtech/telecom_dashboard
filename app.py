import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="India Telecom Dashboard", layout="wide")

st.title("📱 India Telecom Subscriber Dashboard (March 2026)")

df = pd.read_csv("trai_data.csv")

st.markdown("---")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Subscribers", f"{df['Total_Subscribers'].sum():,.0f}M")
with col2:
    st.metric("Total States", len(df))
with col3:
    st.metric("Urban Share", f"{(df['Urban_Subscribers'].sum() / df['Total_Subscribers'].sum() * 100):.1f}%")

st.markdown("---")

st.subheader("Top 10 States by Total Subscribers")
df_sorted = df.sort_values('Total_Subscribers', ascending=False).head(10)

fig, ax = plt.subplots(figsize=(12, 6))
ax.barh(df_sorted['Service_Area'], df_sorted['Total_Subscribers'], color='steelblue')
ax.set_xlabel('Total Subscribers (Millions)')
ax.set_title('Top 10 States by Total Telecom Subscribers')
st.pyplot(fig)

st.markdown("---")

st.subheader("Operator Market Share")
operators = ['Bharti_Airtel', 'Reliance_Jio', 'Vodafone_Idea', 'BSNL', 'MTNL']
market_share = {op: df[op].sum() for op in operators}

fig, ax = plt.subplots(figsize=(10, 6))
ax.pie(market_share.values(), labels=market_share.keys(), autopct='%1.1f%%', startangle=90)
ax.set_title('Operator Market Share')
st.pyplot(fig)

st.markdown("---")

st.subheader("Urban vs Rural Subscribers")
urban_total = df['Urban_Subscribers'].sum()
rural_total = df['Rural_Subscribers'].sum()

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(['Urban', 'Rural'], [urban_total, rural_total], color=['#1f77b4', '#ff7f0e'])
ax.set_ylabel('Subscribers (Millions)')
ax.set_title('Urban vs Rural Subscriber Distribution')
st.pyplot(fig)

st.markdown("---")

st.subheader("State-wise Data")
st.dataframe(df)