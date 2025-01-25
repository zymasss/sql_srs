import io
import streamlit as st
import pandas as pd
import duckdb



csv = '''
beverage,price
orange juice, 2.5
expresso, 2
tea, 3'''

beverages = pd.read_csv(io.StringIO(csv))


csv2= '''
food_item, food_price
cookie juice, 2.5
chocolatine, 2
muffin, 3'''

food_items = pd.read_csv(io.StringIO(csv2))

answer = '''
SELECT * from beverages
CROSS JOIN food_items'''

solution = duckdb.sql(answer).df()


with st.sidebar:
    option = st.selectbox(
        "WHat would like to review?",
        ("Join", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme..."
    )
    st.write("You selected:", option)

query  = st.text_area(label="entrez votre input")

if query:
    result=duckdb.sql(answer).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(['Tables','Solution'])

with tab2:
    st.write('table: beverages')
    st.dataframe(beverages)
    st.write('table:food_items')
    st.dataframe(food_items)
    st.write('expected')
    st.dataframe(solution)

with tab3:
    st.write(answer)
