'''Basic use of for '''
# 1) create list of 1 to 15 numbers ....
ls = [i for i in range(16)]
print("list : ", ls)

# 2) create dictionary of 1 to 15 numbers ....
d = {i:f"data{i}"   for i in range(15)}
print("\n dict : ", d)



''' use condition  & advance '''
# 1) create list even no`s btn 1 to 15 ....
ls = [i for i in range(16) if i % 2]
print("\n even-list : ", ls)

print()
#generator 
g = (i for i in range(16))
for i in g:
  print(i, end=" ")

print("\n\nodd list : ",end=" ")
#generat a odd no's btn 1 to 15
odd = (i for i in range(16) if i % 2 != 0)
for i in odd:
  print(i, end=" ")
