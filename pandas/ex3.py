
import pandas as pd

# Read the File
df = pd.read_csv('ex3.csv')

# Add new Column Total
df['Total'] = df['Price'] * df['Quantity']

# Group by product
grouped = df.groupby('Product')['Total'].sum().reset_index()

# Sort by total sales
sorted_off = grouped.sort_values(by='Total', ascending=False)

# Final Output
print("Sales summary")
print(sorted_off)

print(df['Total'])