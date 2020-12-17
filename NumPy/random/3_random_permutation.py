#random permutation

import numpy
from numpy import random

arr = numpy.array([1,2,3,4,5])

#The shuffle() method makes changes to the original array.
random.shuffle(arr)

print(arr)

#Generating Permutation of Arrays....
'''The permutation() method returns are-arranged
array (and leaves the original array un-changed).'''


arr1 = numpy.array([1,2,3,4,5])

print(random.permutation(arr1))
print(arr1)
