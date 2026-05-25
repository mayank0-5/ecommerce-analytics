-- E-commerce Analytics SQL Queries

-- 1. Revenue and Profit by Category
SELECT Category,
       ROUND(SUM(Amount), 2) as Total_Revenue,
       ROUND(SUM(Profit), 2) as Total_Profit
FROM order_details
GROUP BY Category
ORDER BY Total_Revenue DESC;

-- 2. Top 10 States by Revenue
SELECT State,
       ROUND(SUM(Amount), 2) as Total_Revenue,
       COUNT(DISTINCT [Order ID]) as Total_Orders
FROM orders_merged
GROUP BY State
ORDER BY Total_Revenue DESC
LIMIT 10;

-- 3. Monthly Revenue Trend
SELECT strftime('%m', [Order Date]) as month,
       strftime('%Y', [Order Date]) as year,
       ROUND(SUM(Amount), 2) as Monthly_Revenue
FROM orders_merged
GROUP BY year, month
ORDER BY year, month;

-- 4. Top 10 Most Profitable Products
SELECT [Sub-Category],
       ROUND(SUM(Profit), 2) as Total_Profit,
       ROUND(SUM(Amount), 2) as Total_Revenue
FROM order_details
GROUP BY [Sub-Category]
ORDER BY Total_Profit DESC
LIMIT 10;

-- 5. Top 10 Customers by Revenue
SELECT [CustomerName],
       ROUND(SUM(Amount), 2) as Total_Spent,
       COUNT(DISTINCT [Order ID]) as Total_Orders
FROM orders_merged
GROUP BY [CustomerName]
ORDER BY Total_Spent DESC
LIMIT 10;