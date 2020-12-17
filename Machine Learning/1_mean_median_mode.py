#1_mean_median_mode

import numpy
from scipy import stats
#MEAN...
speed = [99, 23, 54, 12, 78, 95, 34, 9, 12, 45, 32]
print("Mean : ",numpy.mean(speed))

#Median...
print("Median : ",numpy.median(speed))

#Mode
print("Mode : ",stats.mode(speed))
'''#The mode() method returns a ModeResult object that contains the mode
number (12),and count (how many times the mode number appeared (2)).
