
SELECT
    COUNT(DISTINCT Invoice) AS Total_Orders,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    ROUND(
        SUM(Revenue) * 1.0 /
        NULLIF(COUNT(DISTINCT Invoice), 0),
        2
    ) AS Average_Order_Value
FROM retail_sales;
