# pylint: disable=missing-module-docstring
import ast

import duckdb
import streamlit as st



#ANSWER_STR = """
#SELECT * from beverages
#CROSS JOIN food_items"""

con = duckdb.connect(database='data/exercices_sql_tables.duckdb', read_only=False)


# solution_df = duckdb.sql(ANSWER_STR).df()


with st.sidebar:
    theme = st.selectbox(
        "WHat would like to review?",
        ("cross_joins", "GroupBy", "window_functions"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected:", theme)


    exercise = con.execute(f"SELECT * FROM memory_state where theme = '{theme}'").df()
    st.write(exercise)

query = st.text_area(label="entrez votre input")
print(con.execute("SHOW TABLES").df())


if query:
    result = con.execute(query).df()
    st.dataframe(result)
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
tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    exercise_tables=ast.literal_eval(exercise.loc[0, "tables"])

    for table in exercise_tables:
        st.write(f"table : {table}")
        df_table = con.execute(f"SELECT * FROM {table}")
        st.dataframe(df_table)

#
with tab3:
    exercise_name = (exercise.loc[0, "exercise_name"])
    with open(f"answers/{exercise_name}", "r") as f:
        answer = f.read()
    st.write(answer)
