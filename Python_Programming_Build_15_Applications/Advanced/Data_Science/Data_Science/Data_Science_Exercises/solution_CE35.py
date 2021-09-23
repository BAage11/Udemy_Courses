import matplotlib.pyplot as plt
import pandas as pan

# Importing data
dt = pan.read_csv('sales_data.csv')
dt1 = dt.copy()  # Creating another dataframe with numeric values
del(dt1['Day'])

# Creating lists to store data for the total, max and min values
tot_lst = []
max_lst = []
min_lst = []

for ind in [0, 1, 2, 3, 4, 5, 6]:
    # Using for loop to pass the index in each iteration to shorten the code
    tot_lst.append(sum(dt1.iloc[ind]))
    max_lst.append(max(dt1.iloc[ind]))
    min_lst.append(min(dt1.iloc[ind]))

# Creating new columns
dt['Total Sales'] = tot_lst
dt['Min Sales'] = min_lst
dt['Max Sales'] = max_lst

# Creating lists to store data for the min, max, average and total sales value for each product
min_sal = []
max_sal = []
avg_sal = []
tot_sal = []

for col in ['ProductA', 'ProductB', 'ProductC', 'ProductE', 'ProductF']:
    # Using for loop to pass the column label in each iteration to shorten the code
    min_sal.append(dt[col].min())
    max_sal.append(dt[col].max())
    avg_sal.append(round(dt[col].mean(), 2))
    tot_sal.append(dt[col].sum())

# Creating the new data frame for the statistical data
df = pan.DataFrame({
    'Min Sales': min_sal,
    'Max Sales': max_sal,
    'Avg. Sales': avg_sal,
    'Total Sales': tot_sal
}, index=['ProductA', 'ProductB', 'ProductC', 'ProductE', 'ProductF'])

# Printing the data
print('Sales Report\n')
print(dt, end='\n\n')
print('Products Statistics\n')
print(df)

# visualization
for col in ['ProductA', 'ProductB', 'ProductC', 'ProductE', 'ProductF']:
    plt.plot(dt['Day'], dt[col])
    plt.title(col)
    plt.ylabel('Sales')
    plt.show()
