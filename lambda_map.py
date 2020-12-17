# print square...
from functools import reduce
ls = [1, 2, 3, 4, 5, 6, 7, 8]

# type 1) using function...


def sqr(num):
    return num*num


# use of map
map_obj = map(sqr, ls)
print("using normal fuction : ", end=" ")
for item in map_obj:
    print(item, end=", ")

# type 2) using lambda function....

map_obj2 = map(lambda num: num*num, ls)
print("\nusing lambda fuction  : ", end=" ")
for item in map_obj2:
    print(item, end=", ")

# type 3)


def square(num):
    return num*num


def cube(num):
    return num*num*num


func_list = [square, cube]
print()
for item in range(5):
    print(list(map(lambda x: x(item), func_list)))

######### Filter ###########
ls = [4, 8, 4, 6, 55, 4, 9, 5, 3, 2, 12, 15]


def is_greter(num):
    return num > 5


data = list(filter(is_greter, ls))
print("Filter : ", data)

# ---------reduse------
data = reduce(lambda x, y: x+y, ls)
print("reduce : ", data)
