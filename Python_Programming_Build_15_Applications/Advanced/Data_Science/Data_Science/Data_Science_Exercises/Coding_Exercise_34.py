import pandas as pd

data = pd.read_csv('Advanced/Data_Science/Data_Science_Exercises/data.csv')

data['Name'] = data['First name'] + " " + data['Last name']

del data['First name']
del data['Last name']

data = data[['Name', 'Identifier', 'Department',
             'Location', 'Access code', 'Recovery code']]

data_set = {}
for column in ['Name', 'Department', 'Location', 'Access code', 'Recovery code']:
    data_set[column] = data[column].tolist()

new_data = pd.DataFrame(data_set, index=data['Identifier'].tolist())

# data.set_index('Identifier', inplace=True)
print(new_data)
