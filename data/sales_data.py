import pandas as pd
import numpy as np

# Generate random sales data
np.random.seed(42)
dates = pd.date_range(start='2021-01-01', end='2023-12-31', freq='D')
products = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch']
regions = ['North', 'South', 'East', 'West']

# Create random data
data = {
    'date': np.random.choice(dates, size=1500),
    'product': np.random.choice(products, size=1500),
    'region': np.random.choice(regions, size=1500),
    'quantity_sold': np.random.randint(1, 20, size=1500),
    'unit_price': np.random.uniform(50, 2000, size=1500),
    'discount': np.random.uniform(0, 0.3, size=1500)
}

# Calculate revenue
sales_data = pd.DataFrame(data)
sales_data['revenue'] = sales_data['quantity_sold'] * sales_data['unit_price'] * (1 - sales_data['discount'])

# Save to CSV
sales_data.to_csv('data/sales_data.csv', index=False)

print("Sales data generated and saved to data/sales_data.csv.")
