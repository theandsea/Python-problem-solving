import random


def count_paths(m,n,blocks):
    """
    find the number of connected paths between the top-left square and the bottom right square by traversing only the intermediate squares with the . symbol
    m is the number of rows and n is the number of columns
    :param m:
    :param n:
    :param blocks:
    :return:
    """
    assert isinstance(m,int) and isinstance(n,int) and isinstance(blocks,list)
    for tup in blocks:
        assert isinstance(tup,tuple)

    # initial
    grid=[[0 for j in range(n)] for i in range(m)]
    for (x,y) in blocks:
        grid[x][y]=-1

    # DP, using a stack for each step
    """"""
    grid[0][0]=1
    prest=[(0,0)]
    afterst=[]
    while len(prest)>0:
        while len(prest):
            (x,y)=prest.pop()
            num=grid[x][y]
            if x+1<m and grid[x+1][y] != -1:
                if grid[x+1][y] == 0: # not added yet
                    afterst.append((x+1,y))
                grid[x + 1][y] += num
            if y+1<n and grid[x][y+1] != -1:
                if grid[x][y+1] ==0:
                    afterst.append((x,y+1))
                grid[x][y+1] += num
        prest,afterst = afterst,prest
        # print(prest)

    return grid[m-1][n-1]


"""
print(count_paths(3,4,[(0,3),(1,1)]))
print(count_paths(3,3,[]))
"""

print(random.randrange(4))