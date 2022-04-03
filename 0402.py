def map_bitstring(x):
    """
    takes a list of bitstrings (i.e., 0101) and
    maps each bitstring to 0 if the number of 0s in the bitstring strictly exceeds the number of 1s.
    Otherwise, map that bitstring to 1
    :param x:
    :return:
    """
    assert isinstance(x,list)
    for bitstr in x:
        assert bitstr.replace("0","").replace("1","")=="" # strictly bitstring

    res={}
    for bitstr in x:
        if bitstr not in res.keys():
            if len(bitstr.replace("1",""))>len(bitstr.replace("0","")): # only 0 left > only 1 left
                res[bitstr]=0
            else:
                res[bitstr]=1

    return res

"""
x= ['100', '100', '110', '010', '111', '000', '110', '010', '011', '000']
print(map_bitstring(x))
"""
