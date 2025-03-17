SELECT
    store_id,
    SUM(amount) AS total_sales,
    SUM(amount) FILTER (WHERE product_name = 'redbull') AS redbull_sales,
    ROUND(
        SUM(amount) FILTER (WHERE product_name = 'redbull') * 100.0 / SUM(amount), 2
    ) AS redbull_share
FROM redbulls
GROUP BY store_id