import pandas as pd

# Load the sales dataset
file_path = "data/sales_data.csv"

df = pd.read_csv(file_path)
# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])
# Calculate total sales
df["Sales"] = df["Price"] * df["Units_Sold"]

print("\nUpdated data types:")
print(df.dtypes)

# Display basic information
print("Dataset loaded successfully!")
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())
print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

print("\nBasic statistics:")
print(df.describe())
print("\nSales column:")
print(df[["Product_Name", "Price", "Units_Sold", "Sales"]].head())
# -----------------------------
# BUSINESS ANALYSIS
# -----------------------------

total_sales = df["Sales"].sum()
total_units = df["Units_Sold"].sum()
average_sales = df["Sales"].mean()

print("\n--- BUSINESS KPIs ---")
print("Total Sales:", total_sales)
print("Total Units Sold:", total_units)
print("Average Sales per Transaction:", round(average_sales, 2))

# Sales by product
product_sales = df.groupby("Product_Name")["Sales"].sum().sort_values(ascending=False)

print("\n--- SALES BY PRODUCT ---")
print(product_sales)

# Sales by category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print("\n--- SALES BY CATEGORY ---")
print(category_sales)
# -----------------------------
# PROMOTION ANALYSIS
# -----------------------------

promotion_sales = df.groupby("Promotion")["Sales"].agg(
    ["sum", "mean", "count"]
)

print("\n--- PROMOTION ANALYSIS ---")
print(promotion_sales)

promotion_units = df.groupby("Promotion")["Units_Sold"].mean()

print("\n--- AVERAGE UNITS SOLD ---")
print(promotion_units)
# -----------------------------
# MONTHLY SALES ANALYSIS
# -----------------------------

df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n--- MONTHLY SALES ---")
print(monthly_sales)

best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()

worst_month = monthly_sales.idxmin()
worst_month_sales = monthly_sales.min()

print("\nBest Month:", best_month)
print("Best Month Sales:", best_month_sales)

print("\nWorst Month:", worst_month)
print("Worst Month Sales:", worst_month_sales)
# -----------------------------
# SAVE PROCESSED DATA
# -----------------------------

output_path = "data/cleaned_sales_data.csv"
df.to_csv(output_path, index=False)

print("\nProcessed dataset saved successfully!")
print("File location:", output_path)
print("Final dataset shape:", df.shape)