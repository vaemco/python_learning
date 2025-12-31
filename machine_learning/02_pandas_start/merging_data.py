import pandas as pd

products = {
    "Product_ID": [101, 102, 103],
    "Name" : ["Laptop", "Maus", "Tastatur"],    
}
sales = {
    "Sale_ID": [1, 2, 3, 4],
    "Product_ID": [101, 101, 102, 104],
    "Quantity": [5, 2, 10, 1]
}
products = pd.DataFrame(products)
sales = pd.DataFrame(sales)

merged_df = pd.merge(sales,products, on="Product_ID", how="left")
print(merged_df)
