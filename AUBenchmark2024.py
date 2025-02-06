import streamlit as st
import pandas as pd
import plotly.express as px

## Title

st.title('Australian Water Benchmark 2024')

## Import data

finance = pd.read_csv('data/finance.csv')

## User Selections

indicators = finance['Indicator Name'].unique()

x = st.selectbox('Select x-axis indicator', indicators)
y = st.selectbox('Select y-axis indicator', indicators)
filters = [x,y]

## Data Processing
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

st.divider()
st.caption("Data source: [Urban national Performance Report 2023-24: Urban Water Utilities](http://www.bom.gov.au/water/npr/)")
st.caption("Developed by: [Ditiphatra (Hima) Chanarithichai](https://github.com/Kurohima17)")