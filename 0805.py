import math
import numpy as np

def euclid2(a,b):
    s=0
    for i in range(len(a)):
        s += (a[i]-b[i])**2
    return s

def find_convex_cover(pvertices,clist):
    """
    compute the radii, 0≤ri, of m circles centered at those m points such that the sum of the areas of the circles is minimized (approximately) and that any vertex in P is also contained in at least one of the m circles.
    :param pvertices:
    :param clist:
    :return:
    """
    # assert isinstance(pvertices,list)
    assert isinstance(clist,list) # -- center
    #for p in pvertices:
    #    assert isinstance(p,list)
    for c in clist:
        assert isinstance(c,tuple)

    center=clist # center
    v=pvertices # vertice--goal
    n=len(clist)
    r2=[0.0 for i in range(n)] # r square
    for pv in v:
        # greedy find the minimum
        dat2=euclid2(pv,center[0]) - r2[0] # dat square
        index=0
        for i in range(n):
            dat2_i=euclid2(pv,center[i]) - r2[i]
            if dat2 >= dat2_i:
                dat2 = dat2_i
                index=i
        # set
        if dat2 > 0: # <=0 means already contains
            r2[index] += dat2
        # r2[index] = euclid2(pv,center[index])

    r=[0.0 for i in range(n)]
    for i in range(n):
        r[i]=math.sqrt(r2[i])
    return r

"""
pvertices = np.array([[ 0.573,  0.797],
                        [ 0.688,  0.402],
                        [ 0.747,  0.238],
                        [ 0.802,  0.426],
                        [ 0.757,  0.796],
                        [ 0.589,  0.811]])

clist = [(0.7490863467660889, 0.4917635308023209),
              (0.6814339441396109, 0.6199470305156477),
              (0.7241617773773865, 0.6982813914515696),
              (0.6600700275207232, 0.7516911829987891),
              (0.6315848053622062, 0.7730550996176769),
              (0.7348437356868305, 0.41342916986639894),
              (0.7597683050755328, 0.31729154508140384)]

print(find_convex_cover(pvertices,clist))
"""

