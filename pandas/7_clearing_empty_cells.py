import pandas as pd

#remove  empty cells = rows 
# # type 1
df  = pd.read_csv('./data.csv')
# new_df = df.dropna()
# print(new_df.to_string())

# type 2
# Note: Now, the dropna(inplace = True)
# will NOT return a new DataFrame, but it will remove all rows containg NULL values from the original DataFrame
df.dropna(inplace = True)
print(df.to_string())