SELECT year, region, SUM(population)
FROM populations
GROUP BY
GROUPING SETS ((year, region), year)