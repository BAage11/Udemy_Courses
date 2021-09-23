import pandas

dt = {
    'Monday': [27, 56, 32, 21, 44],
    'Tuesday': [15, 51, 22, 40, 32],
    'Wednesday': [34, 41, 19, 17, 25],
    'Thursday': [22, 55, 37, 26, 25],
    'Friday': [27, 49, 32, 31, 44],
    'Saturday': [13, 56, 54, 33, 40],
    'Sunday': [21, 44, 31, 29, 38]
}

sales = pandas.DataFrame(data=dt.values(), index=dt.keys(), columns=[
    'ProductA', 'ProductB', 'ProductC', 'ProductE', 'ProductF'])

print(sales)
