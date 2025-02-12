# pylint: disable=missing-module-docstring
import ast

import os
import logging
import duckdb
import streamlit as st


if "data" not in os.listdir():
    logging.error(os.listdr())
    logging.error("creating folder data")
    os.mkdir("data")

if "exercices_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())

con = duckdb.connect(database='data/exercices_sql_tables.duckdb', read_only=False)

with st.sidebar:
    available_theme_df = con.execute(f"SELECT DISTINCT * from memory_state").df()
    theme = st.selectbox(
        "WHat would like to review?",
        available_theme_df["theme"].unique(),
        index=None,
        placeholder="Select a theme...",
    )
    if theme:
        st.write(f"You selected {theme}")
        select_exercise_query = f"SELECT * FROM memory_state where theme = '{theme}'"
    else:
        select_exercise_query = f"SELECT * FROM memory_state where"

    exercise=(
        con.execute(select_exercise_query)
        .df()
        .sort_values('last_reviewed')
        .reset_index(drop=True))

    st.write(exercise)
    exercise_name = (exercise.loc[0, "exercise_name"])
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()

st.header("Enter your code :")
query = st.text_area(label="entrez votre input")

if query:
    result = con.execute(query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are mising")

    n_line_diffenrece = result.shape[0] - solution_df.shape[0]
    if n_line_diffenrece != 0:
        st.write(
            f"result has a {n_line_diffenrece} lines difference with the solution_df"
        )


tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    exercise_tables=exercise.loc[0, "tables"]

    for table in exercise_tables:
        st.write(f"table : {table}")
        df_table = con.execute(f"SELECT * FROM {table}")
        st.dataframe(df_table)


with tab3:
    st.text(answer)
