import types
"""x
from time import sleep
import random
from datetime import datetime
import itertools as it


def producer():
    'produce timestamps'
    starttime = datetime.now()
    while True:
        sleep(random.uniform(0, 0.2)) # not necessary is 0.2 for test
        yield datetime.now() - starttime
"""

def tracker(p,limit):
    """
    a generator that tracks the output of this producer and ultimately returns the number of odd numbered seconds that have been iterated over.
    :param p:
    :param limit:
    :return:
    """
    assert isinstance(limit,int) and isinstance(p,types.GeneratorType) # p=generator ??
    assert limit>=0
    while True:
        x=next(p)
        receive=(yield x.seconds)
        if receive is not None:
            limit=int(receive)
            assert limit>=0
        if x.seconds >= limit:
            break

"""
p=producer()
t=tracker(p,limit=2)
print(next(t))
t.send(3)
print(list(t))
"""