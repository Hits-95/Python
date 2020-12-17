def gen(num):
    for i in range(num):
        yield i


if __name__ == "__main__":
    gen_obj = gen(10)

    # for i in gen_obj:
    #     print(i)

    ls = [i for i in gen_obj]
    print("l1", ls)

    l = {i for i in gen_obj}
    print("l", l)
