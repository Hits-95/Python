#Searching Arrays
"""search certain value, and return the indexes that get a match.
To search an array, use the where() method.
It returns indexes tuple & dtype of array
"""
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

#find the index where values are even

arr = np.array([1,2,3,4,44,7,6,9])
evenIndexes = np.where(arr  % 2 == 0)
print(evenIndexes)

#find the index where values are eveb searchsorted()
#1) single value search
result = np.searchsorted(arr,44)
print("index",result)

#2) search from right side'
result = np.searchsorted(np.array([1,2,3,4,5]),5,side='right')
print("index : ",result)

#Multiple Values
x = np.searchsorted(np.array([5,4,3,2,1]), [2, 4, 6])

print(x)
