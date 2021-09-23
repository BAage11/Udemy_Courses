import pandas as pd

data = pd.read_csv(
    'Advanced/Data_Science/Data_Science_Exercises/sales_data.csv')

# Create header list, to iterate over for finding 'Min Sales' and 'Max Sales'
headers = ['ProductA', 'ProductB', 'ProductC', 'ProductE', 'ProductF']

# Creating dataframe of data
sales_df = pd.DataFrame(data)

# Change type of columns to float, so mathematical operations can be executed on them
sales_df['ProductA'] = sales_df['ProductA'].astype(float)
sales_df['ProductB'] = sales_df['ProductB'].astype(float)
sales_df['ProductC'] = sales_df['ProductC'].astype(float)
sales_df['ProductE'] = sales_df['ProductE'].astype(float)
sales_df['ProductF'] = sales_df['ProductF'].astype(float)

# Create a new column, summing up each row (sum up column : axis=0)
sales_df['Total Sales'] = sales_df.sum(axis=1)

# Get the name of product with minimum sale each day
sales_df['Min Sales'] = sales_df[headers].idxmin(axis=1)

# Get the name of product with maximum sale each day
sales_df['Max Sales'] = sales_df[headers].idxmax(axis=1)

# Minimum sale per product found
productA_min = sales_df['ProductA'].min()
productB_min = sales_df['ProductB'].min()
productC_min = sales_df['ProductC'].min()
productE_min = sales_df['ProductE'].min()
productF_min = sales_df['ProductF'].min()

# Maximum sale per product found
productA_max = sales_df['ProductA'].max()
productB_max = sales_df['ProductB'].max()
productC_max = sales_df['ProductC'].max()
productE_max = sales_df['ProductE'].max()
productF_max = sales_df['ProductF'].max()

# Average sale per product
productA_avg = round(sales_df['ProductA'].mean(), 2)
productB_avg = round(sales_df['ProductB'].mean(), 2)
productC_avg = round(sales_df['ProductC'].mean(), 2)
productE_avg = round(sales_df['ProductE'].mean(), 2)
productF_avg = round(sales_df['ProductF'].mean(), 2)

# Total sale per product
productA_total = sales_df['ProductA'].sum()
productB_total = sales_df['ProductB'].sum()
productC_total = sales_df['ProductC'].sum()
productE_total = sales_df['ProductE'].sum()
productF_total = sales_df['ProductF'].sum()

# Create a new dataframe with calculated results of each product
prod_df = pd.DataFrame({'Min Sales': [productA_min, productB_min, productC_min, productE_min, productF_min],
                        'Max Sales': [productA_max, productB_max, productC_max, productE_max, productF_max],
                        'Avg. Sales': [productA_avg, productB_avg, productC_avg, productE_avg, productF_avg],
                        'Total Sales': [productA_total, productB_total, productC_total, productE_total, productF_total]}, index=['ProductA', 'ProductB', 'ProductC', 'ProductE', 'ProductF'])

# Change floating numbers to integers, except 'Avg. Sales' column
prod_df['Min Sales'] = prod_df['Min Sales'].astype(int)
prod_df['Max Sales'] = prod_df['Max Sales'].astype(int)
prod_df['Total Sales'] = prod_df['Total Sales'].astype(int)


# Print out the tables (dataframes)
print('Sales Report')
print(sales_df, end='\n \n')

print('Product Statistics')
print(prod_df)
