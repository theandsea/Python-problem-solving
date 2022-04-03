def area(seq,a,b):
    remain=min(seq[a],seq[b])
    s = 0
    for i in range(a+1,b):
        s += remain-seq[i]
    return s

def get_trapped_water(seq):
    """
    Compute how many units of water remain trapped between the walls in the map.
    :param seq:
    :return:
    """
    assert isinstance(seq,list) and len(seq)>=2
    for num in seq:
        assert isinstance(num,int)

    pairs=list(zip(seq,range(len(seq))))
    pairs=sorted(pairs,key=lambda x:x[0])
    l,r=pairs[-1][1],pairs[-2][1]
    # l_h,r_h=pairs[-1][0],pairs[-2][0]
    if l>r:
        l,r=r,l
        # l_h,r_h=r_h,l_h
    s = area(seq,l,r)
    for i in reversed(range(len(pairs)-2)):
        p=pairs[i][1]
        if p<l:
            s += area(seq,p,l)
            l=p
        elif r<p:
            s += area(seq,r,p)
            r=p
    return s

# print(get_trapped_water([2,1,2]))
# print(get_trapped_water([3, 0, 1, 3, 0, 5]))