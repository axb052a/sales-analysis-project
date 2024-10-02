# Load cleaned data
sales_data = pd.read_csv('data/cleaned_sales_data.csv')

# Add 'month' column and group by month to calculate total revenue
sales_data['month'] = pd.to_datetime(sales_data['date']).dt.to_period('M')
monthly_sales = sales_data.groupby('month')['revenue'].sum().reset_index()

# Check data types before plotting
print(monthly_sales.dtypes)

# Ensure correct data types
monthly_sales['month'] = monthly_sales['month'].astype(str)
monthly_sales['revenue'] = pd.to_numeric(monthly_sales['revenue'], errors='coerce')

# Plot sales trends
plt.figure(figsize=(10, 6))
sns.lineplot(x='month', y='revenue', data=monthly_sales)
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visuals/revenue_trends.png')
plt.show()
