import pandas as pd 

data = pd.read_json('./data.json')
df = pd.DataFrame(data)
print(df)