import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("ecommerce.db")
print("Connected to database!")

# Query 1: Total Revenue and Profit by Category
print("\n--- Revenue and Profit by Category ---")
q1 = pd.read_sql_query("""
    SELECT Category,
           ROUND(SUM(Amount), 2) as Total_Revenue,
           ROUND(SUM(Profit), 2) as Total_Profit,
           COUNT(DISTINCT od.[Order ID]) as Total_Orders
    FROM order_details od
    JOIN orders o ON od.[Order ID] = o.[Order ID]
    GROUP BY Category
    ORDER BY Total_Revenue DESC
""", conn)

# Query 2: Top 10 States by Revenue
print("\n--- Top 10 States by Revenue ---")
q2 = pd.read_sql_query("""
    SELECT State,
           ROUND(SUM(Amount), 2) as Total_Revenue,
           COUNT(DISTINCT [Order ID]) as Total_Orders
    FROM orders_merged
    GROUP BY State
    ORDER BY Total_Revenue DESC
    LIMIT 10
""", conn)
print(q2.to_string(index=False))

# Query 3: Monthly Revenue Trend
print("\n--- Monthly Revenue Trend ---")
q3 = pd.read_sql_query("""
    SELECT strftime('%m', [Order Date]) as month,
           strftime('%Y', [Order Date]) as year,
           ROUND(SUM(Amount), 2) as Monthly_Revenue,
           COUNT(DISTINCT [Order ID]) as Total_Orders
    FROM orders_merged
    GROUP BY year, month
    ORDER BY year, month
""", conn)

# Query 4: Top 10 Most Profitable Products
print("\n--- Top 10 Most Profitable Products ---")
q4 = pd.read_sql_query("""
    SELECT [Sub-Category],
           ROUND(SUM(Profit), 2) as Total_Profit,
           ROUND(SUM(Amount), 2) as Total_Revenue
    FROM order_details
    GROUP BY [Sub-Category]
    ORDER BY Total_Profit DESC
    LIMIT 10
""", conn)
print(q4.to_string(index=False))

# Query 5: Top 10 Customers by Revenue
print("\n--- Top 10 Customers by Revenue ---")
q5 = pd.read_sql_query("""
    SELECT [CustomerName],
           ROUND(SUM(Amount), 2) as Total_Spent,
           COUNT(DISTINCT [Order ID]) as Total_Orders
    FROM orders_merged
    GROUP BY [CustomerName]
    ORDER BY Total_Spent DESC
    LIMIT 10
""", conn)
print(q5.to_string(index=False))

conn.close()
print("\nAll queries done!")