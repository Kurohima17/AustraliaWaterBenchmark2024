import streamlit as st
import pandas as pd
import plotly.express as px

## Title

st.title('Australian Water Benchmark 2024')

## Import data

finance = pd.read_csv('data/finance.csv')

## Placeholder for user sliders and dropdowns

x = 'Total income for the utility'
y = 'Economic real rate of return: water supply'
filters = [x,y]
# Filter the dataframe
filtered = finance[finance['Indicator Name'].isin(filters)]
filtered = filtered.filter(items=['Area','Utility','Indicator Name','2023-2024']).reset_index(drop=True)
filtered = filtered.pivot_table(index=['Area','Utility'], columns='Indicator Name', values='2023-2024').reset_index()
# Remove rows with missing values in 'Area' column to ensure data have equal length
filtered = filtered.dropna(subset=['Area', x, y])

## Scatter plot

fig = px.scatter(filtered,
           x=x,
           y=y,
           color='Area',
           hover_name='Utility')

st.plotly_chart(fig)