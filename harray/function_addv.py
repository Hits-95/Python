# ----------- Assine function to variable -------------
def add(num1, num2):
    return num1 + num2


var_add = add  # assine
print("before delete : ", var_add(5, 10))
del add  # delete the add function

# till addition is work bcoz of object of add() func is assing to var_add variable...
print("after delete : ", var_add(20, 10))


# ----------- Return a fuction -------------
def returnFuc(num):
    if num:
        return print  # print means print()
    else:
        return sum  # sum means sun()


print("pass 1 : ", returnFuc(1))
print("pass 0 : ", returnFuc(0))

# ---------- pass function as argument ---------


def executor(func):
    func("hitesh")


# calling...........
executor(print)
