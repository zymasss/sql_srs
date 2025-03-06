import io
import pandas as pd
import duckdb

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# ------------------------------------------------------------
# EXERCISES LIST
# ------------------------------------------------------------

data = {
    "theme": ["cross_joins", "cross_joins", "case_when", "case_when", "case_when"],
    "exercise_name": ["beverages_and_food", "sizes_and_trademarks", "employees_and_wage", "orders_discout", "employees_sal_range"],
    "tables": [["beverages", "food_items"], ["sizes", "trademarks"], ['employees'], ["orders"], ['employees']],
    "last_reviewed": ["1980-01-01", "1970-01-01", "1970-01-01", "1970-01-01", "1970-01-01"],
    "instructions" : ["Affiche toutes les combinaisons de menus disponibles.",
                      "Affiche pour toutes les tailles pour toutes les marques.",
                      "Appliquez une augmentation de 10% pour l'IT, 5% pour l'HR, 3% pour les SALES et 0% pour les autres.",
                      "Créez une CTE intégrant une expression CASE WHEN afin de calculer une nouvelle colonne nommée total_revenue, prenant en compte les réductions appliquées. Ensuite, utilisez cette table intermédiaire pour calculer le revenu total après déduction des réductions. (ordre décroissant)",
                      "Utilisez une CTE pour créer une colonne 'salary_range' avec 'Low' quand salaires < à 50 000, 'Medium' < à 90 000, et 'High' pour les autres. Calculez la moyenne des salaires pour chaque catégorie et affichez le nombre de personnes incluses dans chaque regroupement."],
}
memory_state_df = pd.DataFrame(data)
con.execute("CREATE OR REPLACE TABLE memory_state AS SELECT * FROM memory_state_df")


# ------------------------------------------------------------
# CROSS JOIN EXERCISES
# ------------------------------------------------------------
csv = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(csv))
con.execute("CREATE OR REPLACE TABLE beverages AS SELECT * FROM beverages")

csv2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(csv2))
con.execute("CREATE OR REPLACE TABLE food_items AS SELECT * FROM food_items")


sizes = """
size
XS
M
L
XL
"""
sizes = pd.read_csv(io.StringIO(sizes))
con.execute("CREATE OR REPLACE TABLE sizes AS SELECT * FROM sizes")

trademarks = """
trademark
Nike
Asphalte
Abercrombie
Lewis
"""
trademarks = pd.read_csv(io.StringIO(trademarks))
con.execute("CREATE OR REPLACE TABLE trademarks AS SELECT * FROM trademarks")

employees = """
name,wage,department
Toufik,60000,IT
Jean-Nicolas,75000,HR
Daniel,55000,SALES
Kaouter,80000,IT
Sylvie,70000,IT
Sebastien,90000,HR
Diane,65000,SALES
Romain,72000,IT
François,68000,HR
Anna,85000,SALES
Zeinaba,100000,IT
Gregory,120000,IT
Karima,95000,HR
Arthur,83000,SALES
Benjamin,110000,CEO
"""

employees = pd.read_csv(io.StringIO(employees))
con.execute("CREATE OR REPLACE TABLE employees AS SELECT * FROM employees")


orders = """
order_id,product_id,quantity,price_per_unit,discount_code
1,101,5,10.0,None
2,102,3,25.0,DISCOUNT10
3,101,2,10.0,DISCOUNT20
4,103,4,8.0,None
5,102,6,25.0,None
6,103,2,8.0,UNKNOWN
"""

orders = pd.read_csv(io.StringIO(orders))
con.execute("CREATE OR REPLACE TABLE orders AS SELECT * FROM orders")


con.close()
