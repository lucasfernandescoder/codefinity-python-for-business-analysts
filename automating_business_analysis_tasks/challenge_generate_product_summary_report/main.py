def generate_product_report(summary_dict):
    # Write your code here
    lines = []
    total_revenue = 0
    for product, data in summary_dict.items():
        line = f"Product: {product}, Units Sold: {data['units_sold']}, Revenue: ${data['revenue']:.2f}"
        lines.append(line)
        total_revenue += data["revenue"]
    total_line = f"Total Revenue: ${total_revenue:.2f}"
    lines.append(total_line)
    return "/n".join(lines)
        

summary = {
    "Widget": {"units_sold": 120, "revenue": 2400.00},
    "Gadget": {"units_sold": 75, "revenue": 1500.50},
    "Thingamajig": {"units_sold": 200, "revenue": 5000.00}
}
report = generate_product_report(summary)
print(report)
