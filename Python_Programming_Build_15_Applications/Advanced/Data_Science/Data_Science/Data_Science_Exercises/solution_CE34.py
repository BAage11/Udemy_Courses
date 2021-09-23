import pandas as pan

dt = pan.read_csv('Advanced/Data_Science/Data_Science_Exercises/data.csv')

dt['Name'] = dt['First name'] + dt['Last name']

del(dt['Last name'])
del(dt['First name'])

dt = dt[['Name', 'Identifier', 'Department',
         'Location', 'Access code', 'Recovery code']]

data_set = dict()

for col in ['Name', 'Department', 'Location', 'Access code', 'Recovery code']:
    data_set.update({col: dt[col].tolist()})

df = pan.DataFrame(data_set, index=dt['Identifier'].tolist())

print(df)
