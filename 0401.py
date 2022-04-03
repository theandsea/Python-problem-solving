import random


def get_sample(nbits=3,prob=None,n=1):
    """
    return a list n of random samples from a finite probability mass function defined by a dictionary with keys defined by a specified number of bits
    :param nbits:
    :param prob:
    :param n:
    :return:
    """
    assert isinstance(nbits,int) and isinstance(prob,dict) and isinstance(n, int)
    assert nbits>=1 and n>=1
    # check total probability
    s=0.0
    sample=[]
    upper=[]
    for key in prob.keys():
        assert prob[key]>=0
        s += prob[key]
        sample.append(key)
        upper.append(s)
    assert s==1.0

    res=[]
    for i in range(n):
        seed=random.random()
        print(seed)
        for j in range(len(prob)):
            if seed<=upper[j]:
                res.append(sample[j])
                break
    return res

"""
p={'000': 0.125,
 '001': 0.125,
 '010': 0.125,
 '011': 0.125,
 '100': 0.125,
 '101': 0.125,
 '110': 0.125,
 '111': 0.125}
print(get_sample(nbits=3,prob=p,n=4))
"""

