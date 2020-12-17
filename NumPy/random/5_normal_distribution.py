#norma distrubution
from numpy import random
import matplotlib.pyplot as ptl
import seaborn as sbn

print(random.normal(size = (2,3)))

#Generate a random normal distribution of
#size 2x3 with mean at 1 and standard deviation of 2:

print(random.normal(loc = 1, scale = 2, size = (2,3)))


#Visualization of Normal Distribution
sbn.distplot(random.normal(size = 1000), hist = False)
ptl.show()

