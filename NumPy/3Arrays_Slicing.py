#NumPy Array Slicing...
# 1) we pass slice instead of index like this : [start:end]
# 2) we can also define a STEP like this : [start:end:step]
# start = 0, end = lenght of array

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr[-7::])
