import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

os.makedirs("visualizations", exist_ok=True)

# Load Dataset
df = pd.read_csv("sales_data.csv")

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# 1 Sales Trend
sales_trend = df.groupby("Date")["Total_Sales"].sum()

plt.figure(figsize=(8,5))
sales_trend.plot()
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.savefig("visualizations/sales_trend.png")
plt.close()

# 2 Product Sales
product_sales = df.groupby("Product")["Total_Sales"].sum()

plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Product Sales")
plt.savefig("visualizations/product_sales.png")
plt.close()

# 3 Region Sales
region_sales = df.groupby("Region")["Total_Sales"].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Region Sales")
plt.savefig("visualizations/region_sales.png")
plt.close()

# 4 Box Plot
plt.figure(figsize=(8,5))
sns.boxplot(y=df["Total_Sales"])
plt.title("Sales Distribution")
plt.savefig("visualizations/boxplot.png")
plt.close()

# 5 Heatmap
numeric_df = df.select_dtypes(include="number")

plt.figure(figsize=(8,5))
sns.heatmap(numeric_df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("visualizations/heatmap.png")
plt.close()

# Interactive Plotly Chart
fig = px.line(
    df,
    x="Date",
    y="Total_Sales",
    color="Region",
    title="Interactive Sales Dashboard"
)

fig.write_html("visualizations/dashboard.html")

print("Dashboard Created Successfully")