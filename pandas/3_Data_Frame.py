# Data Frame is like an array or table its behave like row and colm

import pandas as pd
data = {
    'Name': ['Hitesh Ahire', 'Suyash Ahire', 'Shbham Jagtap'],
    'Age': [22, 28, 21]
}

# load data into dataframe object
df = pd.DataFrame(data)
print(df, end='\n+++++++++++++++++++++++\n')

""" Locate Row """
print(df.loc[1], end='\n+++++++++++++++++++++++\n')

print(df.loc[[0, 1]], end='\n+++++++++++++++++++++++\n')

# Named index
df = pd.DataFrame(data, index=['data1', 'data2', 'data3'])
print(df)
