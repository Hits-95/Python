#Data Distribution....
# choice...
'''The probability is set by a number between 0 and 1,
where 0 means that the value will never occur and 1 means that the value will always occur.'''


from numpy import random

print(random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100)))

#2-D array


print(random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(5,8)))




