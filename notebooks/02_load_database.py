import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv("data/cleaned_data.csv")
orders = pd.read_csv("data/List of Orders.csv")
details = pd.read_csv("data/Order Details.csv")
target = pd.read_csv("data/Sales target.csv")

print("Data loaded!")

# Create SQLite database
conn = sqlite3.connect("ecommerce.db")
print("Database created!")

# Load all tables into database
df.to_sql("orders_merged", conn, if_exists="replace", index=False)
orders.to_sql("orders", conn, if_exists="replace", index=False)
details.to_sql("order_details", conn, if_exists="replace", index=False)
target.to_sql("sales_target", conn, if_exists="replace", index=False)

print("All tables loaded into database!")

# Verify tables
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("\nTables in database:")
for table in tables:
    print(" -", table[0])

# Check row counts
for table in ["orders", "order_details", "sales_target", "orders_merged"]:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table}: {count} rows")

conn.close()
print("\nDatabase ready!")