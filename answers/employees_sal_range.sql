WITH cte_table AS (SELECT
  department, wage,
  CASE
      WHEN wage <= 50000 THEN 'Low'
      WHEN wage < 90000 THEN 'Medium'
      ELSE 'High'
  END AS salary_range,
FROM
  employees)

SELECT department, salary_range, AVG(wage), COUNT(*)
  FROM cte_table
GROUP BY
  department, salary_range