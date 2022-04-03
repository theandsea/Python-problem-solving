import math
import random

def est_prob(n: int, m: int, niter: int = 100) -> float:
    '''
    Write a simulation to estimate the probability
    choose m vertices at random with replacement. What is the probability that the inscribed polygon with m vertices is not degenerate (i.e., actually has m vertices)
    :param n: num sides in regular polygon (n>=4)
    :type n: int
    :param m: num vertices for inscribed polygon (m>=3)
    :type m: int
    :param niter: num iterations for simulation
    :type m: int
    '''
    assert isinstance(n, int) and n >= 4
    assert isinstance(m, int) and 3 <= m <= n
    assert isinstance(niter, int) and niter >= 1

    # simulation just different points
    s = 0
    for i in range(niter):
        plist = random.choices(range(n), k=m)
        # print(plist)
        point = {}
        for p in plist:
            if p not in point:
                point[p] = True
            else:
                s += 1
                # print("--------NO")
                break
    return 1 - s / niter


def get_prob_shape(n: int, m: int, equilateral: bool = False) -> float:
    '''
    what is the probability that the non-degenerate inscribed polygon is equilateral?
    Write a function to return numerical (i.e., not simulated) solution
    :param n: num sides in regular polygon (n>=4)
    :type n: int
    :param m: num vertices for inscribed polygon (m>=3)
    :type m: int
    '''
    assert isinstance(n, int) and n >= 4
    assert isinstance(m, int) and 3 <= m <= n
    assert isinstance(equilateral, bool)

    if equilateral:  # equilateral:
        if n % m == 0:
            # available = n // m  # available points, this is wrong !
            prob = 1
            prob *= n / n  # first
            for i in range(1, m):
                prob *= (m - i) / n
                # print(prob)
            return prob
        else:
            return 0.0
    else:
        prob = 1
        for i in range(m):  # select m points
            prob *= (n - i) / n
        return prob


# print(est_prob(7, 3, 1000000))
# print(get_prob_shape(6, 3,equilateral=True))



