import pandas as pd

# Load dataset
data = pd.read_csv("dataset/sales_data.csv", encoding='latin1')

# Show first 5 rows
print(data.head())

# Dataset information
print(data.info())

# Check missing values
print(data.isnull().sum())

category_sales = data.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)

category_sales = data.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)

import matplotlib.pyplot as plt

region_sales = data.groupby("Region")["Sales"].sum()

region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.show()

# -------------------------------
# Monthly Sales Trend
# -------------------------------
# -------------------------------
# Monthly Sales Trend
# -------------------------------

data['Order Date'] = pd.to_datetime(data['Order Date'], dayfirst=True, errors='coerce')

data['Month'] = data['Order Date'].dt.month

monthly_sales = data.groupby('Month')['Sales'].sum()

print("\nMonthly Sales:")
print(monthly_sales)

monthly_sales.plot(kind='line', marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.show()
