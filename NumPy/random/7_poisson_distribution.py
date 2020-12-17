#Poiddion distribution
from numpy import random
import matplotlib.pyplot as ptl
import seaborn as sbn
'''lam - rate or known number of occurences e.g. 2 for above problem.
size - The shape of the returned array.'''

print(random.poisson(lam = 2, size = 10))

#Visualization of Poisson Distribution
sbn.distplot(random.poisson(lam=2, size=1000), kde=False)
ptl.show()

#Difference Between Normal and Poisson Distribution
sbn.distplot(random.normal(loc = 50,scale = 7, size=1000), label = 'normal', hist=False)
sbn.distplot(random.poisson(lam=2, size=1000), label = 'poisson', hist=False)
ptl.show()
