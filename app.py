import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Nassau Candy Distributor - Shipping Analysis")

df = pd.read_csv('Nassau Candy Distributor.csv')

df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='mixed')
df['Lead Time'] = (df['Ship Date'] - df['Order Date']).dt.days

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Ship Mode Analysis")
ship_mode = df.groupby('Ship Mode')['Lead Time'].mean()
fig1, ax1 = plt.subplots()
ax1.bar(ship_mode.index, ship_mode.values, color='blue')
ax1.set_xlabel('Ship Mode')
ax1.set_ylabel('Days')
st.pyplot(fig1)

st.subheader("Sales by Region")
region_sales = df.groupby('Region')['Sales'].sum()
fig2, ax2 = plt.subplots()
ax2.bar(region_sales.index, region_sales.values, color='green')
st.pyplot(fig2)
