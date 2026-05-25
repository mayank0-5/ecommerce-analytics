import pandas as pd

orders = pd.read_csv("data/List of Orders.csv")
details = pd.read_csv("data/Order Details.csv")

print("Files loaded!")
print("Orders shape:", orders.shape)
print("Details shape:", details.shape)

df = pd.merge(orders, details, on="Order ID", how="inner")
print("Merged shape:", df.shape)
print("Total Revenue:", df["Amount"].sum())
print("Total Profit:", df["Profit"].sum())

df.to_csv("data/cleaned_data.csv", index=False)
print("Cleaned data saved!")