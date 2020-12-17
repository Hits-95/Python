#Binomial distribution...
from numpy import random
import matplotlib.pyplot as sbt
import seaborn as sbn

#Given 10 trials for coin toss generate 10 data points:
print(random.binomial(n = 10, p = 0.5, size = 10))


#Visualization of Binomial Distribution
sbn.distplot(random.binomial(n=10, p=0.5, size=100), hist=True, kde=False)
sbt.show()


#Difference Between Normal and Binomial Distribution
sbn.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sbn.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
sbt.show()

