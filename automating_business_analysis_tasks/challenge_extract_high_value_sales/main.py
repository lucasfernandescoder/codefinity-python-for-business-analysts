def extract_high_value_sales(sales_records):
    # Write your code here
    high_value_sales = []
    for record in sales_records:
        if record.get('revenue', 0) > 1000:
            filtered_record = {
            'date': record.get('date'),
            'product': record.get('product'),
            'revenue': record.get('revenue')
            }
            high_value_sales.append(filtered_record)
    return high_value_sales

# Sample calls
sales_data = [
    {'date': '2024-06-01', 'product': 'Laptop', 'revenue': 1500, 'region': 'West'},
    {'date': '2024-06-01', 'product': 'Mouse', 'revenue': 200, 'region': 'East'},
    {'date': '2024-06-02', 'product': 'Monitor', 'revenue': 1200, 'region': 'North'},
    {'date': '2024-06-02', 'product': 'Keyboard', 'revenue': 700, 'region': 'South'}
]

result = extract_high_value_sales(sales_data)
print(result)
