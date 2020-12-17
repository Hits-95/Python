char = ["a", "b", "c", "d", "f"]
myiter = iter(char)
# NOTE :while running type 1 comment out type 2(from line 13 to 15 ) & when running type 2 comment out type 1(from line 5 to 10) .....IMP
# type 1
# print("iteration using __next__() method")
# print(myiter.__next__())
# print(myiter.__next__())
# print(myiter.__next__())
# print(myiter.__next__())
# print(myiter.__next__())

# type 2
print("iteration using for loop")
for temp in myiter:
    print(temp)

# type 3
print("iteration using for loop")
for temp in char:
    print(temp)

print(type(char))
