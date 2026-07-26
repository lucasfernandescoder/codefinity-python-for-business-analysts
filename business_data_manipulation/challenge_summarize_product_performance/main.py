def summarize_products(sales_records):
    summary = {}
    for record in sales_records:
        product = record['product']
        units = record['units_sold']
        revenue = record['revenue']
        if product not in summary:
            summary[product] = {'units_sold': 0, 'revenue': 0}
        summary[product]['units_sold'] += units
        summary[product]['revenue'] += revenue
    return summary

# Sample calls
sales_data = [
    {'product': 'Widget', 'units_sold': 10, 'revenue': 250},
    {'product': 'Gadget', 'units_sold': 5, 'revenue': 150},
    {'product': 'Widget', 'units_sold': 7, 'revenue': 175},
    {'product': 'Gizmo', 'units_sold': 3, 'revenue': 90},
    {'product': 'Gadget', 'units_sold': 2, 'revenue': 60}
]

summary_result = summarize_products(sales_data)
print(summary_result)
