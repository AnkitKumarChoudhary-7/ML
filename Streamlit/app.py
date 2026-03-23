import streamlit as st
import pandas as pd
import numpy as np

## Title of the Application
st.title("Hello Streamlit")

## Display a simple test
st.write("This is a simple text")

## Create a simple Dataframe
df = pd.DataFrame({
    'first col' : [1,2,3,4],
    'second col' : [10,20,30,40]
})

## Display the DataFrame
st.write("Here is the Dataframe ")
st.write(df)

## Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns = ['a','b','c']
)
st.line_chart(chart_data)
