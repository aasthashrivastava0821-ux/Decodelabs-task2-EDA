# import pandas as pd

# df = pd.read_excel("Dataset for Data Analytics (1).xlsx")

# print(df.head())

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("Dataset for Data Analytics (1).xlsx")

# First 5 rows
print("\nFIRST 5 ROWS")
print(df.head())

# Dataset information
print("\nDATASET INFO")
print(df.info())

# Statistical summary
print("\nSTATISTICAL SUMMARY")
print(df.describe())

# Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Mean Total Price
print("\nMEAN TOTAL PRICE")
print(df["TotalPrice"].mean())

# Median Total Price
print("\nMEDIAN TOTAL PRICE")
print(df["TotalPrice"].median())

# Product count
print("\nPRODUCT COUNT")
print(df["Product"].value_counts())

# Payment methods
print("\nPAYMENT METHODS")
print(df["PaymentMethod"].value_counts())

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Monthly sales trend
df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["TotalPrice"].sum()

print("\nMONTHLY SALES")
print(monthly_sales)

# Bar chart for products
df["Product"].value_counts().plot(kind="bar")

plt.title("Product Sales Count")
plt.xlabel("Product")
plt.ylabel("Count")
plt.show()

# Pie chart for payment methods
df["PaymentMethod"].value_counts().plot(kind="pie", autopct="%1.1f%%")

plt.title("Payment Methods")
plt.ylabel("")
plt.show()

# Line chart for monthly sales
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Boxplot for outliers
plt.boxplot(df["TotalPrice"])

plt.title("Boxplot of TotalPrice")
plt.show()