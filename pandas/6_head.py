import pandas as pd

df = pd.read_csv('./data.csv')

 #it return begining 10 rows if dont specify the row it default value 5
print("head : ",df.head(), end='\n+++++++++++++++++++++++++++++++++++++++++\n') 
#it return end rows if dont specify the row it default value 5 
print("tail : ",df.tail())
#it return info about dataframe
print("Info : ",df.info())
