import pandas as pd
import matplotlib.pyplot as plt

def sales_dashboard():

    df = pd.read_csv("data/sales_data.csv", encoding="latin1")

    total_sales = df["SALES"].sum()

    product_sales = df.groupby("PRODUCTLINE")["SALES"].sum()

    best_product = product_sales.idxmax()

    summary = pd.DataFrame({
        "Total Sales": [total_sales],
        "Best Product Line": [best_product]
    })

    summary.to_csv("output/summary_report.csv", index=False)

    product_sales.to_csv("output/product_sales_report.csv")

    product_sales.plot(kind="bar")

    plt.title("Product Line Wise Sales")

    plt.tight_layout()

    plt.savefig("output/sales_chart.png")

    print("Sales Dashboard Created Successfully")
    print("Total Sales:", total_sales)
    print("Best Product Line:", best_product)