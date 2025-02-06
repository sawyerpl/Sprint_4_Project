# app.py
# import the necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import scipy as sp


# Load the data frame
def load_data():
    vehicles_df = pd.read_csv('vehicles_us.csv')
    vehicles_df['make'] = vehicles_df['model'].str.split(' ').str[0]
    make_types = vehicles_df['make'].unique()
    condition_types = vehicles_df['condition'].unique()

    return vehicles_df, condition_types, make_types

vehicles_df, condition_types, make_types = load_data()


# Create a title the app
st.header('Vehicle Data Analysis')
st.write('It is not a functional application yet. Under construction.')

# create a check box to show the data frame
df_check_box = st.sidebar.checkbox(label = 'Show DataFrame')

if df_check_box:
    st.write(vehicles_df)




# Create a sidebar and a check box 
st.sidebar.title('Settings')
condition_selector = st.sidebar.multiselect(label='Select Vehicle Condition', options=condition_types, default=condition_types)

make_selector = st.sidebar.selectbox(label='Select a Vehicle Make', options=make_types)

filtered_df = vehicles_df[
    (vehicles_df['condition'].isin(condition_selector)) &
    (vehicles_df['make'] == make_selector)
]



average_price_df = filtered_df.groupby('type')['price'].mean().reset_index()



average_price_fig = px.histogram(average_price_df, x='type', y='price',
                                 title='Average Price by Vehicle type manufactured by ' + make_selector + ' and in ' + str(condition_selector) + ' condition')
st.plotly_chart(average_price_fig)







