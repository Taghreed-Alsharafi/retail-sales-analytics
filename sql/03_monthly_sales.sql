
SELECT
    YearMonth,
    COUNT(DISTINCT Invoice) AS Total_Orders,
    ROUND(SUM(Revenue), 2) AS Monthly_Revenue
FROM retail_sales
GROUP BY YearMonth
ORDER BY YearMonth;
