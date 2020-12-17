import time
from functools import lru_cache


@lru_cache(maxsize=2)
def some_work(n):
    time.sleep(3)
    return n


if __name__ == "__main__":
    print("call")
    some_work(3)
    some_work(4)
    some_work(2)
    print("call again")
    some_work(4)
    print("call after 4")
