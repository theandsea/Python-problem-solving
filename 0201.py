
def get_power_of3(n):
    """
    construct any number between 1 and 40
    :param n:
    :return:
    """
    assert isinstance(n,int)

    factor=[1,3,9,27]
    num=[0,0,0,0]
    rest=n+0;
    for num[0] in range(-1,2):
        for num[1] in range(-1,2):
            for num[2] in range(-1, 2):
                for num[3] in range(-1, 2):
                    s=0
                    for i in range(4):
                        s += num[i]*factor[i]
                    if s==n:
                        print(num)
                        return num

    return None;

"""
get_power_of3(10)
"""


