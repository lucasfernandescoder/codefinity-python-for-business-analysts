import matplotlib.pyplot as plt

def plot_monthly_sales(sales_list):
    # Write your code here
    months = ["Jan","Feb","Mar","Apr","May","Jun", "Jul","Aug","Sep","Oct","Nov","Dec"]
    x_labels = months[:len(sales_list)]
    plt.figure(figsize=(8,5))
    plt.plot(x_labels, sales_list, marker = "o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

sample_sales = [1200, 1500, 1700, 1600, 1800, 2000, 2200, 2100, 2300, 2500, 2400, 2600]
plot_monthly_sales(sample_sales)
