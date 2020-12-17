from numpy import random

#return random number from 1 to 100
print(random.randint(100)) 

#Generate Random Array
#The randint() method takes a size parameter
#where you can specify the shape of an array.
print(random.randint(100 ,size = 5)) #or print(random.randint(100 ,size=(5)))

#Generate a 2-D array with 3 rows,
#each row containing 5 random integers from 0 to 100:
print(random.randint(100 ,size = (3,5)))


''' float'''
#rand() method returns a random float between 0 and 1.
print(random.rand())

#Generate a 1-D array containing 5 random floats:
print(random.rand(5))

#Generate a 2-D array with 3 rows, each row containing 5 random numbers:
print(random.rand(3,5))

#Generate Random Number From Array
#choice() method allows you to generate
#a random value based on an array of values.
print(random.choice([1,2,3,4,5,6]))

print(random.choice([1,2,3,4,5,6], size = 5))

print(random.choice([1,2,3,4,5,6], size = (2,3)))
