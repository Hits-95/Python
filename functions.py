#Arbitrsry args , *args
def my_fun(*args):
    for x in args:
        print(x)
    print("lenth of args : {}".format(len(args)))
    
    print("first item : {}".format(args[0]))
    print("last item : {}".format(args[len(args)-1]))
      
    print("data type of first item : {}".format(type(args[0])))
    print("data type of last item : {}".format(type(len(args)-1)))
   
    
#out put
"""
>>> my_fun("hitesh","pd","online",45,23)
hitesh
pd
online
45
23
lenth of args : 5
first item : hitesh
last item : 23
data type of first item : <class 'str'>
data type of last item : <class 'int'>
"""

    
