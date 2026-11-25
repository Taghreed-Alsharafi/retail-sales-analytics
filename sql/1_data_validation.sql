
SELECT
    COUNT(*) AS Total_Rows,
    ROUND(SUM(Revenue), 2) AS Total_Revenue
FROM retail_sales;
