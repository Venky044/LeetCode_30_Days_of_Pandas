#       Rearrange Products Table

# Table: Products
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | store1      | int     |
# | store2      | int     |
# | store3      | int     |
# +-------------+---------+
# product_id is the primary key (column with unique values) for this table.
# Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
# If the product is not available in a store, the price will be null in that store's column.
 
# Problem:
# Write a solution to rearrange the Products table so that each row has (product_id, store, price). 
# If a product is not available in a store, do not include a row with that product_id and store combination in the result table.

# Return the result table in any order.

# The result format is in the following example.
# Example 1:

# Input: 
# Products table:
# +------------+--------+--------+--------+
# | product_id | store1 | store2 | store3 |
# +------------+--------+--------+--------+
# | 0          | 95     | 100    | 105    |
# | 1          | 70     | null   | 80     |
# +------------+--------+--------+--------+
# Output: 
# +------------+--------+-------+
# | product_id | store  | price |
# +------------+--------+-------+
# | 0          | store1 | 95    |
# | 0          | store2 | 100   |
# | 0          | store3 | 105   |
# | 1          | store1 | 70    |
# | 1          | store3 | 80    |
# +------------+--------+-------+
# Explanation: 
# Product 0 is available in all three stores with prices 95, 100, and 105 respectively.
# Product 1 is available in store1 with price 70 and store3 with price 80. The product is not available in store2.

# Solution:
import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # pandas.melt() : Unpivot a DataFrame from wide to long format, optionally leaving identifiers set.
    # id_vars (tuple, list, or ndarray, optional): Column(s) to use as identifier variables.
    # value_vars (tuple, list, or ndarray, optional): Column(s) to unpivot. If not specified, uses all columns that are not set as id_vars.
    return pd.melt(
        products, id_vars='product_id', var_name='store', value_name='price'
    ).dropna()

# or
import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    res = []
    for ind, row in products.iterrows():
        product_id = row['product_id']

        for store in ['store1', 'store2', 'store3']:
            price = row[store]

            if pd.notna(price):
                res.append((product_id, store, price))
    
    return pd.DataFrame(res, columns=['product_id', 'store', 'price'])
