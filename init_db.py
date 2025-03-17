import io
import pandas as pd
import duckdb

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# ------------------------------------------------------------
# EXERCISES LIST
# ------------------------------------------------------------

data = {
    "theme": ["cross_joins", "cross_joins", "case_when", "case_when", "case_when", "full_outer_join", "grouping_sets", "grouping_sets", "grouping_sets"],
    "exercise_name": ["beverages_and_food", "sizes_and_trademarks", "employees_and_wage", "orders_discout", "employees_sal_range", "product_n_store", "population_evol", "sales_redbull", "filter_sales_redbull"],
    "tables": [["beverages", "food_items"], ["sizes", "trademarks"], ['employees'], ["orders"], ['employees'], ["stores","products"], ["populations"], ["redbulls"], ["redbulls"]],
    "last_reviewed": ["1980-01-01", "1970-01-01", "1970-01-01", "1970-01-01", "1970-01-01", "1970-01-01", "1970-01-01", "1970-01-01", "1970-01-01"],
    "instructions" : ["Affiche toutes les combinaisons de menus disponibles.",
                      "Affiche pour toutes les tailles pour toutes les marques.",
                      "Appliquez une augmentation de 10% pour l'IT, 5% pour l'HR, 3% pour les SALES et 0% pour les autres.",
                      "Créez une CTE intégrant une expression CASE WHEN afin de calculer une nouvelle colonne nommée total_revenue, prenant en compte les réductions appliquées. Ensuite, utilisez cette table intermédiaire pour calculer le revenu total après déduction des réductions. (ordre décroissant)",
                      "Utilisez une CTE pour créer une colonne 'salary_range' avec 'Low' quand salaires < à 50 000, 'Medium' < à 90 000, et 'High' pour les autres. Calculez la moyenne des salaires pour chaque catégorie et affichez le nombre de personnes incluses dans chaque regroupement.",
                      "Faire une jointure (outer join) pour rassembler les stores avec le détail des produits",
                      "Utilisez GROUPING SETS pour agréger les données de population par année et région, tout en calculant également le total de la population par année.",
                      "Pour réaliser cette tâche, commencez par créer une requête avec le GROUPING SETS afin d'obtenir la somme des ventes par 'store_id' et 'product_name', ainsi que par 'store_id' seul. Nommez la colonne qui contiendra les sommes des ventes 'sum_amount'. Ensuite, placez cette requête dans une CTE (Common Table Expression) que vous appellerez 'sales_total'. Une fois cela fait, joignez cette CTE avec elle-même en utilisant la colonne 'store_id' pour établir la relation entre les deux instances de la table. À ce stade, vous allez renommer les colonnes comme suit : la colonne 'sum_amount' de la table de gauche deviendra 'product_sum_amount', et la colonne 'sum_amount' de la table de droite sera renommée en 'store_sum_amount'. Filtrez ensuite les résultats pour ne garder que les lignes où la colonne 'product_name' de la table de gauche est égale à 'redbull', et où la colonne 'product_name' de la table de droite est 'NULL'. Enfin, pour rendre la requête plus claire et éviter que la colonne 'product_name' affiche des valeurs 'NULL' lorsque vous regroupez les données par magasin, utilisez la fonction COALESCE pour remplacer ces 'NULL' par 'tout_le_magasin'. Appliquez également cette modification dans la condition de filtrage de l'étape précédente.",
                      "Utilisez une agrégation couplée avec un FILTER pour calculer, pour chaque magasin (store_id), la quantité totale de produits vendus, ainsi que la part des ventes de Red Bull par rapport au total des ventes du magasin."],
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


stores = """
customer_id,customer_name,store_id,product_id
11,Zeinaba,1.0,101.0
11,Zeinaba,1.0,103.0
11,Zeinaba,1.0,105.0
12,Tancrède,2.0,101.0
12,Tancrède,2.0,103.0
13,Israel,3.0,104.0
14,Kaouter,NaN,NaN
15,Alan,4.0,105.0
"""

stores = pd.read_csv(io.StringIO(stores))
con.execute("CREATE OR REPLACE TABLE stores AS SELECT * FROM stores")

products = """
product_id,product_name,product_price
100,Cherry coke,3
101,Laptop,800
103,Ipad,400
104,Livre,30
"""

products = pd.read_csv(io.StringIO(products))
con.execute("CREATE OR REPLACE TABLE products AS SELECT * FROM products")

populations = """
year,region,population
2016,IDF,1010000
2017,IDF,1020000
2018,IDF,1030000
2019,IDF,1040000
2020,IDF,1000000
2016,HDF,910000
2017,HDF,920000
2018,HDF,930000
2019,HDF,940000
2020,HDF,900000
2016,PACA,810000
2017,PACA,820000
2018,PACA,830000
2019,PACA,840000
2020,PACA,950000
"""

populations = pd.read_csv(io.StringIO(populations))
con.execute("CREATE OR REPLACE TABLE populations AS SELECT * FROM populations")


redbulls = """
store_id,product_name,amount
Armentieres,redbull,45
Armentieres,chips,60
Armentieres,wine,60
Armentieres,redbull,45
Lille,redbull,100
Lille,chips,140
Lille,wine,190
Lille,icecream,170
Douai,redbull,55
Douai,chips,70
Douai,wine,20
Douai,icecream,45
"""

redbulls = pd.read_csv(io.StringIO(redbulls))
con.execute("CREATE OR REPLACE TABLE redbulls AS SELECT * FROM redbulls")



con.close()
