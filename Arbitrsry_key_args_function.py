def my_fun(**args):
    print(" print index")
    for x in args:
        print(x)
    print("\n print value ")
    for x in args:
        print(args[x])
        
#out-put
"""my_fun(fname="hitesh",lname="ahire")
print index
fname
lname

 print value 
hitesh
ahire
"""
