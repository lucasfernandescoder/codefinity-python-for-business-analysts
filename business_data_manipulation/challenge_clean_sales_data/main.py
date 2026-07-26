def clean_sales_data(sales_records):
    # Write your code here
    cleaned_records = []
    for record in sales_records:
        cleaned = record.copy()
        if cleaned.get('units_sold') is None:
            cleaned['units_sold'] = 0
        if cleaned.get('revenue') is None:
            cleaned['revenue'] = 0
        prod = cleaned.get('product')
        if isinstance(prod,str):
            cleaned['product'] = prod.title()
        cleaned_records.append(cleaned)
    return cleaned_records
    
sales_data = [
    {'date': '2024-06-01', 'product': 'laptop', 'units_sold': 10, 'revenue': 15000},
    {'date': '2024-06-02', 'product': 'Laptop', 'units_sold': None, 'revenue': 14500},
    {'date': '2024-06-03', 'product': 'tablet', 'units_sold': 5, 'revenue': None},
    {'date': '2024-06-04', 'product': 'SMARTphone', 'units_sold': None, 'revenue': None},
]


cleaned_sales = clean_sales_data(sales_data)
print(cleaned_sales)
