import streamlit as st
import pandas as pd
import duckdb
import streamlit as st

st.write("""
# SQL SRS
Space Repetition System SQL Practice """)

data= {"a": [1,2,3], "b":[4,5,6]}
df=pd.DataFrame(data)


option = st.selectbox(
    "WHat would like to review?",
    ("Join", "GroupBy", "Windows Functions"),
    index=None,
    placeholder="Select a theme..."
)

st.write("You selected:", option)


option = st.selectbox(
    "What would like to review ?",
    ("Join", "GroupBy", "Windows Functions"),
    index=None,
    placeholder="Select a theme"
)

st.write("You selected :", option)

sql_query  = st.text_area(label="entrez votre input")
result = duckdb.query(sql_query).df()
st.write(f"Vous avez installé : {sql_query}")
st.dataframe(result)
