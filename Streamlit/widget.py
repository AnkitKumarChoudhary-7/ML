import streamlit as st
import pandas as pd
##-----------------------------------------------------------------------
st.title("Streamlit Text Input")
name = st.text_input("Enter Your Name : ")
if name:
    st.write(f"Hello, {name}")

##-----------------------------------------------------------------------

age = st.slider("Select your age : ",0,100,25)
st.write(f"Your age is {age}")

##-----------------------------------------------------------------------
options = ["Python","Java","C","JavaScript"]
choice = st.selectbox("Choose your favourite programming language :",options)
st.write(f"You selected {choice} language")

##-----------------------------------------------------------------------

data = {
    "Name": ["Ankit","Abhi","Sai"],
    "Age": [12,32,45],
    "Hobby":["Football","Gaming","Molesting"]
}

df = pd.DataFrame(data)
st.write(df)

##-----------------------------------------------------------------------
upload_file = st.file_uploader("Choose a CSV file",type="csv")
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)
