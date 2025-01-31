# pylint: disable=missing-module-docstring

import duckdb
import streamlit as st



ANSWER_STR = """
SELECT * from beverages
CROSS JOIN food_items"""

con = duckdb.connect(database='data/exercices_sql_tables.duckdb', read_only=False)


# solution_df = duckdb.sql(ANSWER_STR).df()


with st.sidebar:
    theme = st.selectbox(
        "WHat would like to review?",
        ("cross_joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected:", theme)



query = st.text_area(label="entrez votre input")


#if query:
#    result = duckdb.sql(query).df()
#    st.dataframe(result)
#
#    try:
#        result = result[solution_df.columns]
#        st.dataframe(result.compare(solution_df))
#    except KeyError as e:
#        st.write("Some columns are mising")
#
#    n_line_diffenrece = result.shape[0] - solution_df.shape[0]
#    if n_line_diffenrece != 0:
#        st.write(
#            f"result has a {n_line_diffenrece} lines difference with the solution_df"
#        )
#
#
#tab2, tab3 = st.tabs(["Tables", "Solution"])
#
#with tab2:
#    st.write("table: beverages")
#    st.dataframe(beverages)
#    st.write("table:food_items")
#    st.dataframe(food_items)
#    st.write("expected")
#    st.dataframe(solution_df)
#
#with tab3:
#    st.write(ANSWER_STR)
