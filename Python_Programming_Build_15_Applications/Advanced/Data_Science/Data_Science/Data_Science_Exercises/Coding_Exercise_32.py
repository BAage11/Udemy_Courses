import numpy as np
import pandas as pd

arr = np.array([['[1 1]', '[1 2]', '[1 3]'],
                ['[2 1]', '[2 2]', '[2 3]'],
                ['[3 1]', '[3 2]', '[3 3]']])

df = pd.DataFrame(data=arr, index=[1, 2, 3], columns=[
                  'Combo1', 'Combo2', 'Combo3'])

print(df)
