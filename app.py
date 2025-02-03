# app.py
# import the necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import scipy as sp
# Load the data frame
vehicles_df = pd.read_csv('vehicles_us.csv')
vehicles_df['price'] = vehicles_df['price'].astype('float')




# Create a title the app
st.header('Vehicle Data Analysis')
st.write('It is not a functional application yet. Under construction.')
st.write(vehicles_df)

