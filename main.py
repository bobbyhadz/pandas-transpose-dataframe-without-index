# How to Transpose a Pandas DataFrame without index

import pandas as pd


df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'experience': [1, 3, 5, 7],
    'salary': [175.1, 180.2, 190.3, 205.4],
})

print(df)

df.set_index('name', inplace=True)

df = df.transpose()

print('-' * 50)

print(df)