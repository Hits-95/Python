#seaborn ....
import matplotlib.pyplot as ptl
import seaborn as sbn


#Plotting a Distplot With the Histogram
'''sbn.distplot([5,4,3,2,1])
ptl.show()'''

#Plotting a Distplot Without the Histogram

sbn.distplot([5,4,3,2,1], hist = False)

ptl.show()
