import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv(r'C:\Users\pc\Downloads\Nassau Candy Distributor.csv')

# Basic Info
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

# Data Cleaning
df['Order Date'] = pd.to_datetime(df['Order Date'],format='mixed')
df['Ship Date'] = pd.to_datetime(df['Ship Date'],format='mixed')

df['Lead Time'] = (df['Ship Date'] - df['Order Date']).dt.days

print(df.isnull().sum())
print("\nLead Time Stats:")
print(df['Lead Time'].describe())

# Graph 1 - Ship Mode Analysis
ship_mode = df.groupby('Ship Mode')['Lead Time'].mean()
plt.figure(figsize=(8,5))
plt.bar(ship_mode.index, ship_mode.values, color='blue')
plt.title('Average Lead Time by Ship Mode')
plt.xlabel('Ship Mode')
plt.ylabel('Days')
plt.tight_layout()
plt.savefig('ship_mode_analysis.png')
plt.show()
print("Graph 1 saved!")

# Graph 2 - Region wise Sales
region_sales = df.groupby('Region')['Sales'].sum()
plt.figure(figsize=(8,5))
plt.bar(region_sales.index, region_sales.values, color='green')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('region_sales.png')
plt.show()
print("Graph 2 saved!")

# Graph 3 - Top 10 States by Sales
state_sales = df.groupby('State/Province')['Sales'].sum().nlargest(10)
plt.figure(figsize=(10,5))
plt.bar(state_sales.index, state_sales.values, color='orange')
plt.title('Top 10 States by Sales')
plt.xlabel('State')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('state_sales.png')
plt.show()
print("Graph 3 saved!")
# Graph 4 - Monthly Sales Trend
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()
plt.figure(figsize=(12,5))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, color='red', marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('monthly_trend.png')
plt.show()
print("Graph 4 saved!")