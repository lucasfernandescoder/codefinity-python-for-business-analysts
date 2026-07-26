import matplotlib.pyplot as plt

def compare_sales_profit(sales_list, profit_list, product_names):
    # Write your code here
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].bar(product_names, sales_list, color= "skyblue")
    axes[0].set_title("Sales by Product")
    axes[0].set_xlabel("Product")
    axes[0].set_ylabel("Sales")
    axes[1].bar(product_names, profit_list, color= "lightgreen")
    axes[1].set_title("Profit by Product")
    axes[1].set_xlabel("Product")
    axes[1].set_ylabel("Profit")

plt.tight_layout()
plt.show()


# Sample calls
sales = [1000, 1500, 800, 2000]
profits = [200, 300, 100, 400]
products = ['A', 'B', 'C', 'D']
compare_sales_profit(sales, profits, products)
