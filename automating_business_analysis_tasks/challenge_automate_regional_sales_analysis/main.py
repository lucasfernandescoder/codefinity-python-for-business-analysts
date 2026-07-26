def automate_regional_analysis(north_sales, south_sales):
    def clean_sales_data(sales):
        cleaned = []
        for record in sales:
            if not isinstance(record, dict):
                continue
            product = record.get("product")
            sales_value = record.get("sales")
            if not product or sales_value is None:
                continue
            try:
                sales_float = float(sales_value)
            except (ValueError, TypeError):
                continue
            cleaned.append({"product": product.strip(), "sales": sales_float})
        return cleaned

    def summarize_products(sales):
        summary = {}
        for rec in sales:
            p = rec["product"]
            summary[p] = summary.get(p, 0) + rec["sales"]
        return summary

    def generate_report(region, summary):
        lines = [f"Sales Report for {region} Region:"]
        if not summary:
            lines.append("No valid sales data.")
        else:
            for prod, total in sorted(summary.items()):
                lines.append(f"{prod}: {total:.2f}")
        return "\n".join(lines)

    regions = {"North": north_sales, "South": south_sales}
    reports = {}
    for region, sales in regions.items():
        cleaned = clean_sales_data(sales)
        summary = summarize_products(cleaned)
        reports[region] = generate_report(region, summary)
    return reports

if __name__ == "__main__":
    north_sales = [
        {"product": "Widget", "sales": "100.5"},
        {"product": "Gadget", "sales": 85},
        {"product": "Widget", "sales": "invalid"},
        {"product": "Gizmo", "sales": 50},
        {"product": None, "sales": 30},
        "not a dict",
        {"product": "Widget", "sales": 25.0}
    ]

    south_sales = [
        {"product": "Widget", "sales": "75"},
        {"product": "Gadget", "sales": 95.5},
        {"product": "", "sales": 20},
        {"product": "Gizmo", "sales": None},
        {"product": "Gadget", "sales": "10"},
        {"product": "Widget", "sales": 40}
    ]

    result = automate_regional_analysis(north_sales, south_sales)
    print(result["North"])
    print(result["South"])