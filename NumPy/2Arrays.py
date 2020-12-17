#Arrays..
import numpy as np

# 0-D Array...
d0 = np.array(95)
print("0-D Array")
print(d0)

# 1-D Array...
d1 = np.array([1,2,3,4,5,6])
print("1-D Array")
print(d1)

#2-D Array...
d2 = np.array([[1,2,3],[4,5,6]])
print("2-D Array")
print(d2)

#3-D Array...
d3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,9,8]]])
print("3-D Array")
print(d3)

#4-D Array...
d4 = np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[0,9,8]]],[[[1,2,3],[4,5,6]],[[7,8,9],[0,9,8]]],[[[1,2,3],[4,5,6]],[[7,8,9],[0,9,8]]],[[[1,2,3],[4,5,6]],[[7,8,9],[0,9,8]]]])
print("4-D Array")
print(d4)

#Check how many dimentions the arrays have...
print("*** dimentions ***")
print("Do",d0.ndim)
print("D1",d1.ndim)
print("D2",d2.ndim)
print("D3",d3.ndim)
print("D4",d4.ndim)


#Higher Dimention Arrays
print("** Higher Dimention Array **")
arr = np.array([1,2,3,4,5],ndmin = 5)
print(arr)
print("Higher Dimention ",arr.ndim)








