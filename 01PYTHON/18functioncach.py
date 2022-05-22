
import time
from functools import lru_cache

@lru_cache(maxsize=32)
def some_work(n):
    # Some task taking n seconds
    time.sleep(n)
    return n

if __name__=='__main__':
    print("now running some work")
    some_work(3)
    some_work(1)
    some_work(2)
    some_work(2)
    print("Done......Calling again")
    some_work(3)
    some_work(2)
    some_work(1)

    print("called again") 