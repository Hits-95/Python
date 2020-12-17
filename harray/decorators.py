def dec(func_name):
    def now_exicute():
        print("before ...")
        func_name()
        print("after...")
    return now_exicute

# type 2


@dec
def hits():
    print("Hi online.....")


# type 2
hits()
# hits_obj = dec(hits)  # decorator type 1

# hits_obj()
