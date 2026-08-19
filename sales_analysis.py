import pandas as pd

## 1.(Reading the uploaded dataset file)
try:
    df = pd.read_csv('sales_data.csv')
    print("📢 Dataset successfully loaded into the Python environment!\n")
except FileNotFoundError:
    print("❌ Error: sales_data.csv file not found!")
    exit()

## 2.(Calculating Key Metrics)
total_revenue = df['Revenue'].sum()
average_order = df['Revenue'].mean()

print("=========================================")
print("     BUSINESS SALES PERFORMANCE KPIs     ")
print("=========================================")
print(f"🔹 Total Gross Revenue : ${total_revenue:,.2f}")
print(f"🔹 Average Order Value : ${average_order:,.2f}\n")

## 3.(Category Wise Performance Matrix)
print("=========================================")
print("       CATEGORY PERFORMANCE MATRIX       ")
print("=========================================")
category_perf = df.groupby('Category')['Revenue'].sum().reset_index()
category_perf['Market_Share_%'] = (category_perf['Revenue'] / total_revenue) * 100
print(category_perf.sort_values(by='Revenue', ascending=False).to_string(index=False))
print("\n")

## 4.(Regional Sales Contribution)
print("=========================================")
print("       REGIONAL TERRITORY PERFORMANCE     ")
print("=========================================")
regional_perf = df.groupby('Region')['Revenue'].sum().reset_index()
print(regional_perf.sort_values(by='Revenue', ascending=False).to_string(index=False))
