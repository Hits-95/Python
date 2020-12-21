import pandas as pd

a = [1, 2, 3, 4, 5]
myvar = pd.Series(a)

print("Normal output", myvar)

# my var as Lable
myvar = pd.Series(a, index=['v', 'w', 'x', 'y', 'z', ])
print("Lable outPut ", myvar)

# Key/Value Objects as Series
data = {
    'day1': 12,
    'day2': 13,
    'day3': 14,
    'day4': 16,
}
myvar = pd.Series(data)
print("key-value ", myvar)

# indexing
myvar = pd.Series(data, index=['day1', 'day2'])
print("key-value  index", myvar)
