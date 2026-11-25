
SELECT
    StockCode,
    Description,
    SUM(Quantity) AS Units_Sold,
    ROUND(SUM(Revenue), 2) AS Total_Revenue
FROM retail_sales
WHERE Description IS NOT NULL
  AND TRIM(Description) <> ''
GROUP BY StockCode, Description
ORDER BY Total_Revenue DESC
LIMIT 10;
