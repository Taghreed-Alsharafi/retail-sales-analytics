
SELECT
    Country,
    COUNT(DISTINCT Invoice) AS Total_Orders,
    ROUND(SUM(Revenue), 2) AS Total_Revenue
FROM retail_sales
GROUP BY Country
ORDER BY Total_Revenue DESC;
