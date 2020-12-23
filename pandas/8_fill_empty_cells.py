import pandas as pd

df = pd.read_csv('data.csv')
# df.fillna(952017, inplace=True)

# replace specific colm
df['Calories'].fillna(952017, inplace=True)
print(df.to_string())