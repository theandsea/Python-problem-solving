import random

import numpy as np


def gen_rand_slash(m=6, n=6, direction='back'):
    """
    # uniformly random forward or backslashed image of at least 2 pixel
    :param m:
    :param n:
    :param direction:
    :return:
    """
    assert isinstance(m, int) and isinstance(n, int) and isinstance(direction, str)
    assert m >= 2 and n >= 2 and (direction == 'back' or direction == 'forward')

    if direction == 'back':
        fact = 1
    else:
        fact = -1

    # randomly select 1 point
    s=0
    while s < 2:
        arr = np.zeros((m, n))
        a = random.randrange(m)
        b = random.randrange(n)
        s = 0
        x = a + 0
        y = b + 0
        while x < m and n > y >= 0:  # chain
            arr[x][y] = 1
            s += 1
            if random.random() < 0.618:
                x += 1
                y += fact
            else:
                break
        x = a - 1
        y = b - fact
        while x >= 0 and n > y >= 0:
            arr[x][y] = 1
            s += 1
            if random.random() < 0.618:
                x -= 1
                y -= fact
            else:
                break

    return arr



# print(gen_rand_slash(direction='forward'))
