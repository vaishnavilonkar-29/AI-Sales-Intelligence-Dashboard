import pandas as pd
import plotly.express as px

# Load the processed sales dataset
file_path = "data/cleaned_sales_data.csv"

df = pd.read_csv(file_path)

# Ensure correct data types
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Month"].astype(str)

# Calculate monthly sales
monthly_sales = df.groupby("Month", as_index=False)["Sales"].sum()

# Create interactive line chart
fig = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Performance"
)

# Add axis labels
fig.update_layout(
    xaxis_title="Month",
    yaxis_title="Sales"
)

# Display chart
fig.show()
# -----------------------------
# PRODUCT SALES CHART
# -----------------------------

product_sales = df.groupby("Product_Name", as_index=False)["Sales"].sum()

fig2 = px.bar(
    product_sales,
    x="Product_Name",
    y="Sales",
    title="Sales by Product",
    text="Sales"
)

fig2.update_layout(
    xaxis_title="Product",
    yaxis_title="Total Sales"
)

fig2.show()
# -----------------------------
# CATEGORY SALES CHART
# -----------------------------

category_sales = df.groupby("Category", as_index=False)["Sales"].sum()

fig3 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    title="Sales by Category",
    text="Sales"
)

fig3.update_layout(
    xaxis_title="Category",
    yaxis_title="Total Sales"
)

fig3.show()
# -----------------------------
# PROMOTION ANALYSIS
# -----------------------------

promotion_sales = df.groupby("Promotion", as_index=False)["Sales"].sum()

promotion_sales["Promotion"] = promotion_sales["Promotion"].map({
    0: "No Promotion",
    1: "Promotion"
})

fig4 = px.bar(
    promotion_sales,
    x="Promotion",
    y="Sales",
    title="Sales by Promotion Status",
    text="Sales"
)

fig4.update_layout(
    xaxis_title="Promotion Status",
    yaxis_title="Total Sales"
)

fig4.show()